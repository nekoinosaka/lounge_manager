# app/models/beverage.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Beverage(Base):
    __tablename__ = "beverage"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    description = Column(String)
    is_available = Column(Integer, default=1)
