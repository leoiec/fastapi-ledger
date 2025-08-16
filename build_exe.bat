@echo off
REM Compila a un .exe que inicia el webserver local
CALL .venv\Scripts\activate
pip install pyinstaller
pyinstaller --onefile --name ledger-server run_server.py
echo.
echo Ejecutable en: dist\ledger-server.exe
echo Doble clic para iniciar servidor en http://127.0.0.1:8000
