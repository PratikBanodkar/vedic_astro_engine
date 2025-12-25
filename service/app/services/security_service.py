from datetime import datetime
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import Security, HTTPException, Request
from fastapi.security import APIKeyHeader
from cachetools import TTLCache

# Initialize Firebase
# Logic: If GOOGLE_APPLICATION_CREDENTIALS env var is set (Local Docker), it uses that file.
# If not set (Cloud Run), it uses default generic credentials.
# if not firebase_admin._apps:
#     try:
#         firebase_admin.initialize_app()
#     except Exception as e:
#         print(f"Warning: Firebase Auth skipped locally. {e}")
if not firebase_admin._apps:
    try:
        # 1. Try to find the local JSON file first (Mac/Local Docker)
        cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        
        if cred_path and os.path.exists(cred_path):
            print(f"Using local credentials from: {cred_path}")
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        else:
            # 2. Fallback for Cloud Run (Uses the built-in Service Account)
            print("No local credentials found. Using Google Application Default Credentials.")
            firebase_admin.initialize_app()
            
    except Exception as e:
        print(f"Warning: Firebase Auth initialization failed. {e}")

db = None
try:
    db = firestore.client()
    print("Firestore client initialized successfully.") 
except Exception as e:
    print(f"CRITICAL ERROR: Firestore Init Failed: {e}")

API_KEY_HEADER = APIKeyHeader(name="X-Api-Key", auto_error=True)
ADMIN_KEY_ENV_VAR = "ADMIN_API_KEY"

# Cache keys for 10 minutes to save money
api_key_cache = TTLCache(maxsize=1000, ttl=600)

async def validate_api_key(request: Request, api_key: str = Security(API_KEY_HEADER)):
    # 1. GOD MODE (Environment Variable)
    admin_secret = os.getenv(ADMIN_KEY_ENV_VAR)
    print("Validating API Key...")
    print("Received parameter api_key:", api_key)
    if admin_secret and api_key == admin_secret:
        print("Admin access granted.")
        request.state.user_role = "admin"
        request.state.user_id = "god_mode"
        return api_key

    # 2. CACHE CHECK
    if api_key in api_key_cache:
        print("API Key found in cache.")
        data = api_key_cache[api_key]
        request.state.user_role = data.get("role", "free")
        request.state.user_id = data.get("email", "unknown")
        return api_key

    # 3. FIRESTORE CHECK
    if db:
        try:
            doc = db.collection("api_keys").document(api_key).get()

            if doc.exists:
                data = doc.to_dict()
                if data.get("active", True) is False:
                    # Found but explicitly inactive
                    raise HTTPException(status_code=403, detail="API Key Deactivated")

                # Cache it
                api_key_cache[api_key] = data
                request.state.user_role = data.get("role", "free")
                request.state.user_id = data.get("email", "unknown")
                return api_key
            else:
                # Document not found -> unauthorized
                raise HTTPException(status_code=401, detail="Invalid API Key")

        except HTTPException:
            # Propagate explicit 401/403 above
            raise
        except Exception as e:
            # Unexpected DB error; surface as 500
            print(f"DB Error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    # 4. FAIL (no DB available or previous checks didn't return)
    raise HTTPException(status_code=401, detail="Invalid API Key")

def enforce_rate_limit(request: Request, api_key: str = Security(API_KEY_HEADER)):
    role = request.state.user_role
    if role == "admin":
        return

    # api_key: str = Security(API_KEY_HEADER)
    print(f"Enforcing rate limit for role: {role}")
    print(f"API Key for rate limiting: {api_key}")
    # api_key = request.state.api_key
    window = datetime.utcnow().strftime("%Y%m%d%H%M")
    doc_ref = db.collection("rate_limits").document(f"{api_key}_{window}")

    @firestore.transactional
    def txn(transaction):
        snap = doc_ref.get(transaction=transaction)

        if snap.exists:
            count = snap.to_dict().get("count", 0)
            if count >= 5:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            transaction.update(doc_ref, {"count": count + 1})
        else:
            transaction.set(doc_ref, {"count": 1})

    transaction = db.transaction()
    txn(transaction)
