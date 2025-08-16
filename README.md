# FastAPI Ledger (Windows-ready)

## Requisitos
- Windows 10/11
- Python 3.11+ (instalado como `py`)
- PowerShell o CMD

## Desarrollo (auto-reload)

> run_dev.bat

# Guía: cómo descargar y ejecutar el servidor **Ledger** en Windows (sin Git)

## Qué va a obtener
- Una aplicación que corre **solo en su computador** (no sube datos a internet).
- Interfaz web para registrar ingresos/egresos en `http://127.0.0.1:8000/`.

---

## Requisitos previos
- Windows 10 u 11.
- **Python 3.11 o 3.12 (64-bit)** instalado.
- Un navegador web (Edge, Chrome, etc.).
- El **ZIP** del repositorio (descargado desde GitHub).

---

## Paso 1 — Descargar el proyecto como ZIP
1. Abra la página del repositorio en GitHub.
2. Haga clic en el botón verde **Code**.
3. Seleccione **Download ZIP**.
4. Cuando termine, vaya a **Descargas** (o donde lo guardó), **clic derecho → Extraer todo…**  
   → elija un lugar fácil (por ejemplo, el **Escritorio**).

> Quedará una carpeta como `fastapi-ledger` con subcarpetas `app/`, `templates/`, y archivos como `run_dev.bat`, `requirements.txt`, etc.

---

## Paso 2 — Verificar/instalar Python
**Verificar si ya está instalado:**
1. Presione la tecla **Windows**, escriba `cmd` y abra **Símbolo del sistema**.
2. Escriba:
    ```cmd
    py --version
    ```
   Si ve algo como `Python 3.11.x`, ya está listo.

**Si no lo tiene instalado:**
- Instale **Python 3.11/3.12 (64-bit)** desde el instalador (o el pendrive que le compartieron).
- En el instalador, **marque** la casilla **Add Python to PATH** y elija **Install Now**.

---

## Paso 3 — Ejecutar el servidor
1. Abra la carpeta del proyecto que extrajo del ZIP (por ejemplo, `fastapi-ledger`).
2. Haga **doble clic** en **`run_dev.bat`**.
   - La primera vez puede tardar algunos minutos (crea un entorno y descarga componentes).
3. Cuando vea un mensaje similar a:
    ```
    Uvicorn running on http://127.0.0.1:8000
    ```
   deje **esa ventana abierta** (si la cierra, se apaga el servidor).

4. Abra su navegador y visite:
   - **Interfaz:** `http://127.0.0.1:8000/`  
   - **Documentación (opcional):** `http://127.0.0.1:8000/docs`

---

## ¿Cómo se usa?
1. En la página principal complete:
   - **Fecha**
   - **Descripción** (ej.: “Compra supermercado”)
   - **Monto** (ej.: `15000.00`)
   - **Tipo**: `income` (ingreso) o `expense` (egreso)
2. Presione **Agregar**.  
   La nueva fila aparecerá en la tabla y el **Saldo total** se actualizará automáticamente.
3. Mantenga la ventana negra (del servidor) **abierta** mientras usa la app.

---

## Problemas comunes y soluciones

**A) Al hacer doble clic en `run_dev.bat` no pasa nada**  
- Abra la carpeta del proyecto, haga clic en la **barra de dirección**, escriba `cmd` y presione **Enter**.  
  En la ventana que aparece, ejecute:
    ```cmd
    .\run_dev.bat
    ```
- Si Windows pide permisos o firewall, acepte (solo red **privada**).

**B) “Python no se reconoce” o similar**  
- Instale Python 3.11/3.12 (64-bit) con la opción **Add Python to PATH**.  
- Cierre y vuelva a abrir la ventana de comandos y repita.

**C) Se queda instalando o error de internet**  
- Verifique la conexión y ejecute de nuevo `run_dev.bat`.  
  *(En la primera ejecución se necesitan descargar dependencias).*

**D) “Address already in use” (puerto 8000 ocupado)**  
- Cierre otras ventanas del servidor si hay.  
- O use otro puerto:
    ```cmd
    .\.venv\Scripts\activate
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
    ```
  Luego abra `http://127.0.0.1:8001/`.

**E) “Module not found: fastapi/uvicorn”**  
- Asegúrese de haber ejecutado **`run_dev.bat`** (es el que instala todo).  
- Vuelva a ejecutarlo si es necesario.

**F) La página no abre**  
- Verifique que la ventana del servidor muestre “running on http://127.0.0.1:8000”.  
- Si la cerró, ejecute de nuevo `run_dev.bat`.

---

## ¿Cómo apagar el servidor?
- Cierre la ventana del servidor, o presione **Ctrl + C** dentro de esa ventana.
