from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    phone: str
    email: str
    join_date: str
    is_member: int
    
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    join_date: Optional[str] = None
    is_member: Optional[int] = None
    
class CustomerOut(CustomerBase):
    id: int
    
    class Config:
        orm_mode = True