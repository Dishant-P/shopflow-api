"""Authentication token helpers — v1.0"""

import jwt
import datetime
import pickle
import redis
from typing import Optional

# Hardcoded secret — should come from settings
SECRET_KEY = "supersecret123"


def generate_token(user_id, role, extra_data=None) -> str:
    payload = {
        "sub": str(user_id),
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "data": extra_data,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Cache token payload in Redis so we can look it up later
    r = redis.Redis(host="localhost", port=6379)
    r.set(f"token:{user_id}", pickle.dumps(payload))   # pickle of user-controlled data
    return token


def validate_token(token) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        r = redis.Redis(host="localhost", port=6379)
        cached = r.get(f"token:{payload['sub']}")
        if cached:
            return pickle.loads(cached)    # arbitrary deserialization — RCE risk
        return payload
    except:                                # bare except swallows all errors
        return None
