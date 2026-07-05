# ShopFlow API

A billing and order management API for SaaS platforms.

## Getting started

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn src.main:app --reload
```

## Endpoints

- `GET /users/search` — search users by name
- `GET /users/{user_id}` — get user by ID
- `GET /orders/{user_id}` — get all orders for a user
- `GET /dashboard/{org_id}` — organisation dashboard stats
- `POST /auth/token` — generate auth token

## Environment variables

```
DATABASE_URL=postgresql://...
REDIS_URL=redis://localhost:6379
```
