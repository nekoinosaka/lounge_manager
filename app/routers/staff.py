# app/routers/staff.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.staff import StaffCreate, StaffOut, StaffUpdate
from app.crud import staff as crud

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.post("/", response_model=StaffOut)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    return crud.create_staff(db, staff)

@router.get("/", response_model=list[StaffOut])
def read_all_staff(db: Session = Depends(get_db)):
    return crud.get_all_staff(db)

@router.get("/{staff_id}", response_model=StaffOut)
def read_staff(staff_id: int, db: Session = Depends(get_db)):
    db_staff = crud.get_staff(db, staff_id)
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff

@router.put("/{staff_id}", response_model=StaffOut)
def update_staff(staff_id: int, staff: StaffUpdate, db: Session = Depends(get_db)):
    db_staff = crud.update_staff(db, staff_id, staff)
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff not found or update failed")
    print("Updated staff:", db_staff)
    return db_staff