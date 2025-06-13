from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_all_customers(db: Session):
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in customer.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer