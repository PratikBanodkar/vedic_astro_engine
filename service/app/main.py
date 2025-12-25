from fastapi import FastAPI
import os
from .controller.astrology_controller import router as astrology_router

app = FastAPI(title="Vedic Astro Engine")

# CONFIGURATION
EPHE_PATH = os.getenv("EPHE_PATH", "/app/ephe")

# Include routers
app.include_router(astrology_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}