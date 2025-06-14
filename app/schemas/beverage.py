from pydantic import BaseModel
from typing import Optional

class BeverageBase(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    description: Optional[str] = None
    is_available: Optional[int] = 1
    is_deleted: Optional[bool] = False

class BeverageCreate(BeverageBase):
    pass

class BeverageUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    description: Optional[str] = None
    is_available: Optional[int] = None
    is_deleted: Optional[int] = None

class BeverageOut(BeverageBase):
    id: int

    class Config:
        orm_mode = True
