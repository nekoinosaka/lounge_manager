from sqlalchemy.orm import Session
from app.models.beverage import Beverage
from app.schemas.beverage import BeverageCreate, BeverageUpdate

def create_beverage(db: Session, beverage: BeverageCreate) -> Beverage:
    db_bev = Beverage(**beverage.dict())
    db.add(db_bev)
    db.commit()
    db.refresh(db_bev)
    return db_bev

def get_beverage(db: Session, beverage_id: int) -> Beverage:
    return db.query(Beverage).filter(Beverage.id == beverage_id).first()

def get_all_beverages(db: Session):
    return db.query(Beverage).all()

def update_beverage(db: Session, beverage_id: int, beverage: BeverageUpdate) -> Beverage:
    db_bev = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if not db_bev:
        return None
    for field, value in beverage.dict(exclude_unset=True).items():
        setattr(db_bev, field, value)
    db.commit()
    db.refresh(db_bev)
    return db_bev

def delete_beverage(db: Session, beverage_id: int) -> bool:
    db_bev = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if not db_bev:
        return False
    db.delete(db_bev)
    db.commit()
    return True
