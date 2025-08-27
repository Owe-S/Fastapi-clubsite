from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from database import AsyncSessionLocal
from models import NewsArticle

app = FastAPI(
    title="ClubSite Admin Struktur API",
    description="""
    Komplett API-dokumentasjon og datastruktur for adminpanelet i ClubSite.
    Dette API-et gir frontend- og app-utviklere *nøyaktig innsikt* i tabellene, menyene og funksjonene som finnes for de viktigste admin-modulene.
    """,
    version="2.0"
)

# ------------------ FELTMODELLER ------------------

class TableCell(BaseModel):
    tekst: Optional[str] = None
    href: Optional[str] = None
    type: Optional[str] = None
    placeholder: Optional[str] = None
    funksjon: Optional[str] = None

class TableRow(BaseModel):
    celler: List[TableCell]

class TableModel(BaseModel):
    url: str
    kolonner: List[str]
    rader: List[TableRow]

class MenuLink(BaseModel):
    navn: str
    url: str
    ikoner: Optional[List[str]] = None
    underpunkter: Optional[List['MenuLink']] = None

MenuLink.update_forward_refs()

class PageModel(BaseModel):
    navn: str
    url: str
    beskrivelse: Optional[str]
    meny: List[MenuLink]
    tabeller: List[TableModel]

# ---------------- SESSION DEPENDENCY ----------------

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# --------------- NYHET‐SKJEMAER FOR API‐RESPONS/REQUEST ---------------

class NewsOut(BaseModel):
    articleID: int
    heading: str
    ingress: Optional[str]
    validfrom: datetime
    validto: datetime
    boolPubl: bool

    class Config:
        from_attributes = True   # Pydantic v2 erstatning for orm_mode

class NewsIn(BaseModel):
    depID: int
    heading: str
    ingress: Optional[str]
    newscontent: Optional[str]
    validfrom: datetime
    validto: datetime
    boolPubl: bool

# --------------- FAKTISKE DATA (EKSTRAHERT) ---------------

main_menu = [
    MenuLink(navn="Nyheter", url="/admin/news"),
    MenuLink(navn="Undersider", url="/admin/pages"),
    MenuLink(navn="Bilder", url="/admin/images"),
    MenuLink(navn="Dokumenter", url="/admin/documents"),
    MenuLink(navn="Sidemal", url="/admin/template_sub"),
]

# (Her følger dine PageModel-definisjoner som før…)
# nyheter_page, undersider_page, bilder_page, dokumenter_page, sidemal_page

# ------------------- STRUKTUR-ENDPOINTS -------------------

@app.get("/")
def root():
    return {"message": "ClubSite adminstruktur – se /docs for API-endepunkter og struktur"}

@app.get("/struktur/nyheter", response_model=PageModel, tags=["Struktur"])
def hent_nyheter():
    return nyheter_page

@app.get("/struktur/undersider", response_model=PageModel, tags=["Struktur"])
def hent_undersider():
    return undersider_page

@app.get("/struktur/bilder", response_model=PageModel, tags=["Struktur"])
def hent_bilder():
    return bilder_page

@app.get("/struktur/dokumenter", response_model=PageModel, tags=["Struktur"])
def hent_dokumenter():
    return dokumenter_page

@app.get("/struktur/sidemal", response_model=PageModel, tags=["Struktur"])
def hent_sidemal():
    return sidemal_page

# ------------------- HEALTHCHECK -------------------

@app.get("/healthcheck", tags=["Health"])
async def healthcheck(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB healthcheck feilet: {e}")

# ------------------- NYHETER-ENDPOINTS -------------------

@app.get("/news/", response_model=list[NewsOut], tags=["Nyheter"])
async def list_news(session: AsyncSession = Depends(get_session)):
    """
    Henter alle artikler der boolPubl = True, sortert på validfrom synkende.
    """
    stmt = (
        select(NewsArticle)
        .where(NewsArticle.boolPubl == True)
        .order_by(NewsArticle.validfrom.desc())
    )
    result = await session.execute(stmt)
    return result.scalars().all()

@app.post("/news/", response_model=NewsOut, tags=["Nyheter"])
async def create_news(data: NewsIn, session: AsyncSession = Depends(get_session)):
    """
    Oppretter en ny artikkel basert på JSON-data i body.
    """
    new_item = NewsArticle(**data.dict())
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item
