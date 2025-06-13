from fastapi import APIRouter, Depends, HTTPException
from sqlite3 import Connection
from app.database import get_db
from app.schemas.order import Order, OrderCreate, OrderUpdate
import app.crud.order as order_crud
from typing import List

router = APIRouter(prefix="/orders", tags=["Order"])

@router.get("/", response_model=List[Order])
def list_orders(db: Connection = Depends(get_db)):
    return order_crud.get_all_orders(db)

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Connection = Depends(get_db)):
    order = order_crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="订单不存在")
    return order

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Connection = Depends(get_db)):
    return order_crud.create_order(db, order)

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderUpdate, db: Connection = Depends(get_db)):
    updated = order_crud.update_order(db, order_id, order)
    if not updated:
        raise HTTPException(status_code=404, detail="订单不存在")
    return updated

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Connection = Depends(get_db)):
    order_crud.delete_order(db, order_id)
    return {"message": f"订单 {order_id} 已删除"}
