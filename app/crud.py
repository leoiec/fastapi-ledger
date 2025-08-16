from sqlalchemy.orm import Session
from sqlalchemy import select, func
from . import models, schemas

def create_entry(db: Session, data: schemas.EntryCreate) -> models.Entry:
    obj = models.Entry(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_entry(db: Session, entry_id: int):
    return db.get(models.Entry, entry_id)

def list_entries(db: Session, skip: int = 0, limit: int = 50):
    stmt = select(models.Entry).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()

def update_entry(db: Session, entry_id: int, patch: schemas.EntryUpdate):
    obj = get_entry(db, entry_id)
    if not obj:
        return None
    data = patch.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete_entry(db: Session, entry_id: int) -> bool:
    obj = get_entry(db, entry_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

def get_balance(db: Session):
    income = db.query(func.sum(models.Entry.amount)).filter(models.Entry.kind == "income").scalar() or 0
    expense = db.query(func.sum(models.Entry.amount)).filter(models.Entry.kind == "expense").scalar() or 0
    return {"income": float(income), "expense": float(expense), "net": float(income) - float(expense)}
