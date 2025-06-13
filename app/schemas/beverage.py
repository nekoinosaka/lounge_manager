from pydantic import BaseModel
from typing import Optional

class BeverageBase(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    description: Optional[str] = None
    is_available: Optional[int] = 1

class BeverageCreate(BeverageBase):
    pass

class BeverageUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    description: Optional[str] = None
    is_available: Optional[int] = None

class BeverageOut(BeverageBase):
    id: int

    class Config:
        orm_mode = True
