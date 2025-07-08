from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional, AsyncGenerator
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import JWTError, jwt

from database import AsyncSessionLocal
from models import NewsArticle, SiteUser

# ----------------- APP CONFIG -----------------

app = FastAPI(
    title="ClubSite Admin Struktur API",
    description="""
    Komplett API-dokumentasjon og datastruktur for adminpanelet i ClubSite.
    Inkluderer nå OAuth2/JWT-autentisering for SiteUser.
    """,
    version="3.0"
)

# ------------- SECURITY CONFIGURATIONS -------------

SECRET_KEY = "en-veldig-lang-og-tilfeldig-streng"  # bytt til din egen hemmelige nøkkel
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ------------------ Pydantic-modeller ------------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class NewsOut(BaseModel):
    articleID: int
    heading: str
    ingress: Optional[str]
    validfrom: datetime
    validto: datetime
    boolPubl: bool

    class Config:
        from_attributes = True

class NewsIn(BaseModel):
    depID: int
    heading: str
    ingress: Optional[str]
    newscontent: Optional[str]
    validfrom: datetime
    validto: datetime
    boolPubl: bool

# ------------------ STRUKTUR-MODELLER ------------------
# Her legger du inn dine TableCell, TableRow, TableModel, MenuLink, PageModel osv.
# (uendret fra tidligere)

# ---------------- DEPENDENCIES ----------------

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

def verify_password(plain_pw: str, hashed_pw: str) -> bool:
    return pwd_context.verify(plain_pw, hashed_pw)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def get_user(session: AsyncSession, username: str) -> Optional[SiteUser]:
    result = await session.execute(
        select(SiteUser).where(SiteUser.userName == username)
    )
    return result.scalar_one_or_none()

async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await get_user(session, username)
    if not user or not verify_password(password, user.pwdHash or ""):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
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

# ---------------- AUTH ENDPOINT ----------------

@app.post("/token", response_model=Token, tags=["Auth"])
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session)
):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Ugyldig brukernavn eller passord")
    access_token = create_access_token(data={"sub": user.userName})
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------- STRUCTURE ENDPOINTS ----------------

@app.get("/")
def root():
    return {"message": "ClubSite adminstruktur – se /docs for API-endepunkter og struktur"}

# … Dine /struktur/*-endepunkter her …

# ---------------- HEALTHCHECK ----------------

@app.get("/healthcheck", tags=["Health"])
async def healthcheck(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB healthcheck feilet: {e}")

# ---------------- NYHETER ENDPOINTS (beskyttet) ----------------

@app.get("/news/", response_model=list[NewsOut], tags=["Nyheter"])
async def list_news(
    current_user: SiteUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = (
        select(NewsArticle)
        .where(NewsArticle.boolPubl == True)
        .order_by(NewsArticle.validfrom.desc())
    )
    result = await session.execute(stmt)
    return result.scalars().all()

@app.post("/news/", response_model=NewsOut, tags=["Nyheter"])
async def create_news(
    data: NewsIn,
    current_user: SiteUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    new_item = NewsArticle(**data.dict())
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item
