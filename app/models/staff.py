# app/models/staff.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    contact = Column(String)
    hire_date = Column(String, nullable=False)  # 这里可以用 Date 类型，如果你后续愿意处理日期格式
    salary = Column(Float, nullable=False)
    is_active = Column(Integer, default=1)
