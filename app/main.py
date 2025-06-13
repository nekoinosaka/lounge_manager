from fastapi import FastAPI
from app.database import Base, engine
from app.routers import beverage
from app.routers import staff  # 新添加


app = FastAPI()

# 创建表
Base.metadata.create_all(bind=engine)

# 注册路由
app.include_router(beverage.router)
app.include_router(staff.router)
@app.get("/")
def read_root():
    return {"message": "Lounge 管理系统启动成功"}
