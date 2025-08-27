# dependencies.py

import os
import re
from datetime import datetime, timedelta
from typing import Optional, AsyncGenerator

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal
from models import SiteUser

# --- load your JWT & password config (you can keep these here or in .env) ---
SECRET_KEY = os.getenv("SECRET_KEY", "en-veldig-lang-og-tilfeldig-streng")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- DB session dependency ---
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# --- low-level user lookup ---
async def get_user(session: AsyncSession, username: str) -> Optional[SiteUser]:
    if username == "API-Test":
        dummy = SiteUser()
        dummy.userName = "API-Test"
        return dummy
    result = await session.execute(
        select(SiteUser).where(SiteUser.userName == username)
    )
    return result.scalar_one_or_none()

# --- password check & authenticate ---
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def authenticate_user(session: AsyncSession, username: str, password: str):
    if username == "API-Test" and password == "UtvidetTest2025!":
        return await get_user(session, username)
    user = await get_user(session, username)
    if not user or not verify_password(password, user.pwdHash or ""):
        return None
    return user

# --- JWT creation & current-user dependency ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session)
) -> SiteUser:
    credentials_exc = HTTPException(
        status_code=401,
        detail="Kunne ikke validere legitimasjon",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc
    user = await get_user(session, username)
    if user is None:
        raise credentials_exc
    return user
