"""User API endpoints — feat/user-search branch"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import get_db
from src.models import User

router = APIRouter()


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/search")
def search_users(name: str, db: Session = Depends(get_db)):
    # SQL injection: user input concatenated directly into query string
    query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"
    results = db.execute(query).fetchall()
    return results
