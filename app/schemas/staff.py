# app/schemas/staff.py
from pydantic import BaseModel
from typing import Optional

class StaffBase(BaseModel):
    name: str
    position: str
    contact: Optional[str] = None
    hire_date: str
    salary: float
    is_active: Optional[int] = 1

class StaffCreate(StaffBase):
    pass

class StaffUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    contact: Optional[str] = None
    hire_date: Optional[str] = None
    salary: Optional[float] = None
    is_active: Optional[int] = None

class StaffOut(StaffBase):
    id: int

    class Config:
        orm_mode = True
