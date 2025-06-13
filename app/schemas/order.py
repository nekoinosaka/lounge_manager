from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    customer_name: Optional[str] = None
    order_time: datetime
    total_amount: float
    staff_id: Optional[int] = None
class OrderCreate(OrderBase):
    pass
class OrderUpdate(BaseModel):
    customer_name: Optional[str]
    total_amount: Optional[float]
    staff_id: Optional[int]
class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True