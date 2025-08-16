"""
Entry point “auto-arrancable” para Windows.
- Lo puedes ejecutar directamente: python run_server.py
- O compilar a .exe con PyInstaller y abrir el ejecutable.
"""
import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
