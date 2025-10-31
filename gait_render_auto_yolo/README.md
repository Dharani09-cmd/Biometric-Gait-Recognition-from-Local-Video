
# Gait Recognition — Auto YOLOv8 (Render Ready)

This version automatically downloads YOLOv8n weights on first run (no manual upload needed).

Steps:
1. Deploy this ZIP to Render as a new Web Service.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `gunicorn app:app`

At startup, the app:
- Installs ultralytics
- Downloads YOLOv8n model automatically
- Exposes `/` and `/predict` endpoints

