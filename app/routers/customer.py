from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerCreate, CustomerOut, CustomerUpdate
from app.crud import customer as crud
from app.database import get_db

router = APIRouter(prefix="/customers", tags=["Customer"])

@router.post("/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.get("/", response_model=list[CustomerOut])
def get_all_customers(db: Session = Depends(get_db)):
    return crud.get_all_customers(db)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud.delete_customer(db, customer_id)
    return {"message": "Customer deleted"}