from fastapi import FastAPI
from app.database import Base, engine
from app.routers import beverage
from app.routers import staff   
from app.routers import order
from app.routers import customer   
app = FastAPI(
    title="LoungeManage",
    description="Custom Swagger Documentation",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",  # 可选，自定义OpenAPI路径
    docs_url="/docs"  # 可选，自定义文档路径
)

# 创建表
Base.metadata.create_all(bind=engine)

# 注册路由
app.include_router(beverage.router)
app.include_router(staff.router)
app.include_router(order.router)
app.include_router(customer.router)
@app.get("/")
def read_root():
    return {"message": "Lounge 管理系统启动成功"}
