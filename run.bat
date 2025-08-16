@echo off
REM Arranque simple (sin reload)
CALL .venv\Scripts\activate
uvicorn app.main:app --host 127.0.0.1 --port 8000
