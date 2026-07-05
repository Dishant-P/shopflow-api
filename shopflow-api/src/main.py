from fastapi import FastAPI
from src.api.users import router as users_router
from src.api.orders import router as orders_router

app = FastAPI(title="ShopFlow API", version="1.0.0")

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])


@app.get("/health")
def health():
    return {"status": "ok"}
