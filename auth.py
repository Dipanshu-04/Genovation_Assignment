from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

# Dummy database
users = {
    "user1" : "abcd",
    "user2" : "1234"
}

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {user: pwd_context.hash(pw) for user, pw in users.items()}

# JWT settings
SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(username: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    return jwt.encode({"sub": username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
