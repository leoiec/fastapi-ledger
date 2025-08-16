from sqlalchemy import Column, Integer, String, Date, Numeric
from .database import Base

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)
    description = Column(String(255), nullable=False)
    # amount en centavos para evitar float; Numeric también es válido
    amount = Column(Numeric(12, 2), nullable=False)  # positivo ingreso, negativo egreso
    kind = Column(String(20), nullable=False)        # "income" | "expense"
