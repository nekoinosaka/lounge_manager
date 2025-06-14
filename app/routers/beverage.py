from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.beverage import BeverageCreate, BeverageOut, BeverageUpdate
from app.crud import beverage as crud
from app.database import get_db

router = APIRouter(prefix="/beverages", tags=["Beverages"])

@router.post("/", response_model=BeverageOut)
def create_beverage(bev: BeverageCreate, db: Session = Depends(get_db)):
    return crud.create_beverage(db, bev)

@router.get("/", response_model=list[BeverageOut])
def read_all_beverages(db: Session = Depends(get_db)):
    return crud.get_all_beverages(db)

@router.get("/{beverage_id}", response_model=BeverageOut)
def read_beverage(beverage_id: int, db: Session = Depends(get_db)):
    db_bev = crud.get_beverage(db, beverage_id)
    if not db_bev:
        raise HTTPException(status_code=404, detail="Beverage not found")
    return db_bev

@router.put("/{beverage_id}", response_model=BeverageOut)
def update_beverage(beverage_id: int, beverage: BeverageUpdate, db: Session = Depends(get_db)):
    db_bev = crud.update_beverage(db, beverage_id, beverage)
    if not db_bev:
        raise HTTPException(status_code=404, detail="Beverage not found or update failed")
    return db_bev

@router.delete("/{beverage_id}")
def delete_beverage(beverage_id: int, db: Session = Depends(get_db)):
    success = crud.delete_beverage(db, beverage_id)
    if not success:
        raise HTTPException(status_code=404, detail="Beverage not found")
    return {"message": "Beverage deleted successfully"}
@router.delete("/logicalDelete/{beverage_id}")
def logical_delete_beverage(beverage_id: int, db: Session = Depends(get_db)):
    success = crud.logical_delete_beverage(db, beverage_id)
    if not success:
        raise HTTPException(status_code=404, detail="Beverage not found")
    return {"message": "Beverage deleted successfully"}
