"""Order API endpoints — clean baseline"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import get_db
from src.db.queries import get_orders_for_user

router = APIRouter()


@router.get("/{user_id}")
def list_orders(user_id: int, db: Session = Depends(get_db)):
    orders = get_orders_for_user(user_id, db)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return orders
