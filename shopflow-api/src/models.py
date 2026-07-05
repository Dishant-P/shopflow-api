"""Placeholder models — replace with your ORM models"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Permission:
    name: str


@dataclass
class User:
    id: int
    name: str
    org_id: int
    permissions: List[Permission] = field(default_factory=list)


@dataclass
class Product:
    id: int
    name: str
    price: float
    org_id: int


@dataclass
class Order:
    id: int
    user_id: int
    product_id: int
    org_id: int
    quantity: int


@dataclass
class Organisation:
    id: int
    name: str
