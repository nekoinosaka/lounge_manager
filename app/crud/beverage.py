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
    return db.query(Beverage).filter(Beverage.id == beverage_id and Beverage.is_deleted == False).first()

def get_all_beverages(db: Session):
    return db.query(Beverage).filter(Beverage.is_deleted == False).all()

def update_beverage(db: Session, beverage_id: int, beverage: BeverageUpdate) -> Beverage:
    try:
        db_bev = db.query(Beverage).filter(Beverage.id == beverage_id).first()
        if not db_bev:
            return None
        
        # 使用 model_dump 替代弃用的 dict 方法
        beverage_data = beverage.model_dump(exclude_unset=True)
        for field, value in beverage_data.items():
            setattr(db_bev, field, value)
            
        db.commit()
        db.refresh(db_bev)
        return db_bev
        
    except Exception as e:
        db.rollback()  # 发生异常时回滚事务
        raise  # 可以选择重新抛出异常或处理它

def delete_beverage(db: Session, beverage_id: int) -> bool:
    db_bev = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if not db_bev:
        return False
    db.delete(db_bev)
    db.commit()
    return True
def logical_delete_beverage(db: Session, beverage_id: int) -> bool:
    db_bev = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if not db_bev:
        return False
    db_bev.is_deleted = True
    db.commit()
    return True
