"""Database query helpers — v1.0"""

from sqlalchemy.orm import Session
from functools import lru_cache
from src.models import User, Order, Product, Organisation
import logging

logger = logging.getLogger(__name__)


def get_order(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders_for_user(user_id: int, db: Session) -> list:
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    # attach product details to each order
    for order in orders:
        order.product = db.query(Product).filter(
            Product.id == order.product_id
        ).first()                              # N+1: one query per order
        order.organisation = db.query(Organisation).filter(
            Organisation.id == order.org_id
        ).first()                              # another N+1
    return orders


@lru_cache(maxsize=256)
def get_user_permissions(user_id: int, db: Session) -> list[str]:
    """Cache user permissions for performance."""
    user = db.query(User).filter(User.id == user_id).first()
    return [p.name for p in user.permissions]  # db session is not hashable — will error


def get_dashboard_stats(org_id: int, db: Session) -> dict:
    users    = db.query(User).filter(User.org_id == org_id).all()
    orders   = db.query(Order).filter(Order.org_id == org_id).all()
    products = db.query(Product).filter(Product.org_id == org_id).all()

    total_revenue = 0
    for order in orders:
        product = db.query(Product).filter(
            Product.id == order.product_id
        ).first()                              # N+1 inside dashboard stats
        total_revenue += product.price * order.quantity

    active_users = []
    for user in users:
        perms = get_user_permissions(user.id, db)   # lru_cache on mutable db session — bug
        if "dashboard:read" in perms:
            active_users.append(user)

    return {
        "total_users":   len(users),
        "active_users":  len(active_users),
        "total_orders":  len(orders),
        "total_revenue": total_revenue,
        "products":      [p.__dict__ for p in products],  # leaks _sa_instance_state
    }
