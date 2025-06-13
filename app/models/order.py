from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    order_time = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable=False)