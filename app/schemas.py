from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal
from typing import Optional   # ← agrega esto

class EntryBase(BaseModel):
    date: date
    description: str = Field(min_length=1, max_length=255)
    amount: Decimal
    kind: str

    @field_validator("kind")
    @classmethod
    def kind_must_be_valid(cls, v):
        if v not in {"ingreso", "gasto"}:
            raise ValueError("kind must be 'ingreso' or 'gasto'")
        return v

class EntryCreate(EntryBase):
    pass

class EntryUpdate(BaseModel):
    # ↓ reemplaza las uniones con Optional
    date: Optional[date] = None
    description: Optional[str] = None
    amount: Optional[Decimal] = None
    kind: Optional[str] = None

class EntryRead(EntryBase):
    id: int
    class Config:
        from_attributes = True
