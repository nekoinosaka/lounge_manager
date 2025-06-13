# app/crud/staff.py
from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

def create_staff(db: Session, staff: StaffCreate) -> Staff:
    db_staff = Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_staff(db: Session, staff_id: int) -> Staff:
    return db.query(Staff).filter(Staff.id == staff_id).first()

def get_all_staff(db: Session):
    return db.query(Staff).all()

def update_staff(db: Session, staff_id: int, staff: StaffUpdate) -> Staff:
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not db_staff:
        return None
    for field, value in staff.dict(exclude_unset=True).items():
        setattr(db_staff, field, value)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def delete_staff(db: Session, staff_id: int) -> bool:
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not db_staff:
        return False
    db.delete(db_staff)
    db.commit()
    return True
