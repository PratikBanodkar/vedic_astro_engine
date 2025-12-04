# Vedic Astro Engine (Swiss Ephemeris Microservice)

This repository is a fully containerized FastAPI microservice that exposes
Swiss Ephemeris calculations for:

- Planet positions
- Birth chart (Ascendant, MC, cusps)

It uses **pyswisseph** and loads ephemeris files from a directory specified
by the environment variable:

    EPHEMERIS_PATH=/path/to/ephemeris/files

Ephemeris files are **not included** in this repo. You must download them
from official Swiss Ephemeris sources and place them in local-ephe/ or a
GCS bucket.

## Local Setup

1. Install Python 3.11

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
cd service
pip install -r requirements.txt
```
4. Create a folder:
```bash
mkdir ../local-ephe
./download-ephemeris.sh ../local-ephe
```
5. Run locally:
```bash
export EPHEMERIS_PATH="../local-ephe"
python start.py
```
6. Test:
```bash
curl http://localhost:8080/health
```
## Docker Usage

Build:
```bash
docker build -t vedic-astro:local ./service
```
Run:
```bash
docker run --rm -p 8080:8080 \
-e EPHEMERIS_PATH=/ephe \
-v $(pwd)/local-ephe:/ephe \
vedic-astro:local 
```

## Deployment on Cloud Run

1. Upload ephemeris files:
```bash
gsutil -m cp local-ephe/* gs://YOUR_BUCKET
```
2. Deploy:
```bash
gcloud run deploy vedic-astro-engine \
--image <artifact registry image> \
--set-env-vars EPHEMERIS_GCS_BUCKET=YOUR_BUCKET \
--set-env-vars EPHEMERIS_PATH=/ephe \
--region us-central1
```

The container automatically downloads ephemeris from GCS on startup.