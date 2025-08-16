from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal

from .database import Base, engine, get_db
from . import schemas, crud, models

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ledger API", version="0.1.0")

# ---- API JSON (sigue igual) -------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/entries", response_model=schemas.EntryRead, status_code=201)
def create_entry(payload: schemas.EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db, payload)

@app.get("/entries", response_model=list[schemas.EntryRead])
def list_entries(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.list_entries(db, skip=skip, limit=limit)

@app.get("/entries/{entry_id}", response_model=schemas.EntryRead)
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    obj = crud.get_entry(db, entry_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Entry not found")
    return obj

@app.patch("/entries/{entry_id}", response_model=schemas.EntryRead)
def update_entry(entry_id: int, patch: schemas.EntryUpdate, db: Session = Depends(get_db)):
    obj = crud.update_entry(db, entry_id, patch)
    if not obj:
        raise HTTPException(status_code=404, detail="Entry not found")
    return obj

@app.delete("/entries/{entry_id}", status_code=204)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_entry(db, entry_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.get("/balance")
def balance(db: Session = Depends(get_db)):
    return crud.get_balance(db)

# ---- UI con Jinja2 + HTMX ---------------------------------------------------
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def ui_home(request: Request, db: Session = Depends(get_db)):
    rows = crud.list_entries(db, limit=100)
    return templates.TemplateResponse("index.html", {"request": request, "rows": rows})

@app.get("/ui/rows", response_class=HTMLResponse)
def ui_rows(request: Request, db: Session = Depends(get_db)):
    rows = crud.list_entries(db, limit=100)
    return templates.TemplateResponse("rows.html", {"request": request, "rows": rows})

@app.post("/ui/entries", response_class=HTMLResponse)
def ui_create(
    request: Request,
    db: Session = Depends(get_db),
    date: date = Form(...),
    description: str = Form(...),
    amount: Decimal = Form(...),
    kind: str = Form(...)
):
    payload = schemas.EntryCreate(
        date=date, description=description, amount=amount, kind=kind
    )
    obj = crud.create_entry(db, payload)
    # Devolvemos una sola fila para insertar en la tabla
    return templates.TemplateResponse("row.html", {"request": request, "row": obj})
