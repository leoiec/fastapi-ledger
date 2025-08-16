@echo off
REM Activa entorno y arranca con auto-reload
IF NOT EXIST .venv (
  py -m venv .venv
)
CALL .venv\Scripts\activate
py -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
