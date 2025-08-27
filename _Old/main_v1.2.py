from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# --- NYE IMPORTS FOR DATABASE-NYHETER ---
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

# ... resten av filen uendret ...

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

# --------------- FAKTISKE DATA (EKSTRAHERT) ---------------

main_menu = [
    MenuLink(navn="Nyheter", url="/admin/news"),
    MenuLink(navn="Undersider", url="/admin/pages"),
    MenuLink(navn="Bilder", url="/admin/images"),
    MenuLink(navn="Dokumenter", url="/admin/documents"),
    MenuLink(navn="Sidemal", url="/admin/template_sub"),
]

# 1. NYHETER
nyheter_tabell = TableModel(
    url="https://skigk.no/csadmin/news",
    kolonner=[
        "ID", "Vis", "Sort", "Tittel", "Avdeling", "Publisert", "Utløpsdato", "Opprettet", "Forfatter", "Handling"
    ],
    rader=[
        TableRow(celler=[
            TableCell(tekst="81", type="int", placeholder="ID"),
            TableCell(tekst="", href="files_news/aj_news_action?mission=showarticle&articleID=2630", funksjon="Vis artikkel"),
            TableCell(tekst="", funksjon="Sortering"),
            TableCell(tekst="Siste innspurt – din gave dobles! Dine 200,- blir til 400,-", href="news?show=edit&articleID=2630", type="tekst", placeholder="Tittel"),
            TableCell(tekst="Klubb", type="tekst", placeholder="Avdeling"),
            TableCell(tekst="", funksjon="Publiser/Avpubliser"),
            TableCell(tekst="24.06.2025", type="dato", placeholder="Publiseringsdato"),
            TableCell(tekst="26.06.2025", type="dato", placeholder="Utløpsdato"),
            TableCell(tekst="Owe Stangeland", type="tekst", placeholder="Forfatter"),
            TableCell(tekst="", funksjon="Rediger/Slett")
        ]),
        # Flere rader kan legges til her...
    ]
)

nyheter_page = PageModel(
    navn="Nyheter",
    url="/admin/news",
    beskrivelse="Modul for å publisere og administrere nyhetsartikler i ClubSite admin.",
    meny=main_menu,
    tabeller=[nyheter_tabell]
)

# 2. UNDERSIDER
undersider_tabell = TableModel(
    url="https://skigk.no/csadmin/pages",
    kolonner=[
        "Pri", "Vis", "Sort", "Navn på side", "Hjem", "Dir", "Mod", "Vedl", "Opprettet", "Av", "Slett"
    ],
    rader=[
        TableRow(celler=[
            TableCell(tekst="1", type="int", placeholder="Prioritet"),
            TableCell(tekst="", href="files_pages/aj_pages_action?mission=showpage&menuID=9&pageID=96", funksjon="Vis side"),
            TableCell(tekst="", funksjon="Sortering"),
            TableCell(tekst="Ski Cup – Singel Match Play 2025", href="pages?show=edit&pageID=96", type="tekst", placeholder="Tittel"),
            TableCell(tekst="", funksjon="Hjem"),
            TableCell(tekst="", funksjon="Dir"),
            TableCell(tekst="", funksjon="Mod"),
            TableCell(tekst="1", funksjon="Vedlegg"),
            TableCell(tekst="20.05.2025", type="dato", placeholder="Opprettet"),
            TableCell(tekst="Owe Stangeland", type="tekst", placeholder="Forfatter"),
            TableCell(tekst="", funksjon="Slett"),
        ]),
        # Flere rader...
    ]
)

undersider_page = PageModel(
    navn="Undersider",
    url="/admin/pages",
    beskrivelse="Administrer undersider/innholdssider i nettstedet.",
    meny=main_menu,
    tabeller=[undersider_tabell]
)

# 3. BILDER
bilder_tabell = TableModel(
    url="https://skigk.no/csadmin/images?categoryID=0",
    kolonner=["#", "Bilde", "Filnavn", "Kategori", "Opplastet", "Størrelse", "Dimensjoner", "Brukes i", "Slett"],
    rader=[
        TableRow(celler=[
            TableCell(tekst="1"),
            TableCell(tekst="", funksjon="Vis bilde"),
            TableCell(tekst="bilde1.jpg", type="tekst", placeholder="Filnavn"),
            TableCell(tekst="Profilbilder", type="tekst", placeholder="Kategori"),
            TableCell(tekst="26.06.2025", type="dato", placeholder="Opplastet"),
            TableCell(tekst="45KB", type="tekst", placeholder="Størrelse"),
            TableCell(tekst="800x600", type="tekst", placeholder="Dimensjoner"),
            TableCell(tekst="Nyheter", type="tekst", placeholder="Brukes i"),
            TableCell(tekst="", funksjon="Slett")
        ])
    ]
)

bilder_page = PageModel(
    navn="Bilder",
    url="/admin/images",
    beskrivelse="Opplasting og organisering av bilder og illustrasjoner.",
    meny=main_menu,
    tabeller=[bilder_tabell]
)

# 4. DOKUMENTER
dokumenter_tabell = TableModel(
    url="https://skigk.no/csadmin/documents",
    kolonner=["Type", "Info", "Beskrivelse", "Filnavn", "", "Lastet opp", "Slett"],
    rader=[
        TableRow(celler=[
            TableCell(tekst="PDF", type="tekst", placeholder="Filtype"),
            TableCell(tekst="Styremøte referat", type="tekst", placeholder="Info"),
            TableCell(tekst="Referat fra styremøte 24.06.2025", type="tekst", placeholder="Beskrivelse"),
            TableCell(tekst="styremote_2025.pdf", type="tekst", placeholder="Filnavn"),
            TableCell(tekst="", funksjon="Last ned"),
            TableCell(tekst="24.06.2025", type="dato", placeholder="Lastet opp"),
            TableCell(tekst="", funksjon="Slett")
        ]),
        # Flere rader...
    ]
)

dokumenter_page = PageModel(
    navn="Dokumenter",
    url="/admin/documents",
    beskrivelse="Laste opp, organisere og slette dokumenter og filer.",
    meny=main_menu,
    tabeller=[dokumenter_tabell]
)

# 5. SIDEMAL
sidemal_tabell = TableModel(
    url="https://skigk.no/csadmin/template_sub",
    kolonner=["ID", "Navn", "Type", "Beskrivelse", "Sist brukt", "Rediger", "Slett"],
    rader=[
        TableRow(celler=[
            TableCell(tekst="12", type="int", placeholder="ID"),
            TableCell(tekst="Standard mal", type="tekst", placeholder="Navn"),
            TableCell(tekst="Forside", type="tekst", placeholder="Type"),
            TableCell(tekst="Mal for forsidevisning", type="tekst", placeholder="Beskrivelse"),
            TableCell(tekst="21.06.2025", type="dato", placeholder="Sist brukt"),
            TableCell(tekst="", funksjon="Rediger"),
            TableCell(tekst="", funksjon="Slett")
        ]),
        # Flere rader...
    ]
)

sidemal_page = PageModel(
    navn="Sidemal",
    url="/admin/template_sub",
    beskrivelse="Rediger og administrer sidemaler for ulike deler av nettstedet.",
    meny=main_menu,
    tabeller=[sidemal_tabell]
)

# ------------------- ENDPOINTS -------------------

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

@app.get("/healthcheck", tags=["Health"])
async def healthcheck(session: AsyncSession = Depends(get_session)):
    """
    Enkel DB-sjekk: kjører SELECT 1 mot SQL Server,
    returnerer { "status": "ok" } hvis alt fungerer.
    """
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB healthcheck feilet: {e}")
