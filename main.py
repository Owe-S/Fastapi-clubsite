from fastapi import FastAPI

# Import schemas so models are available to FastAPI docs
import schemas  # noqa: F401

from routes import nyheter, undersider, bilder, dokumenter, sidemal


app = FastAPI(
    title="ClubSite Admin Struktur API",
    description="""
    Komplett API-dokumentasjon og datastruktur for adminpanelet i ClubSite.
    Dette API-et gir frontend- og app-utviklere *nøyaktig innsikt* i tabellene, menyene og funksjonene som finnes for de viktigste admin-modulene.
    """,
    version="2.0",
)

# Include routers under /struktur prefix
app.include_router(nyheter.router, prefix="/struktur", tags=["Struktur"])
app.include_router(undersider.router, prefix="/struktur", tags=["Struktur"])
app.include_router(bilder.router, prefix="/struktur", tags=["Struktur"])
app.include_router(dokumenter.router, prefix="/struktur", tags=["Struktur"])
app.include_router(sidemal.router, prefix="/struktur", tags=["Struktur"])


@app.get("/", summary="Root - Velkommen")
def root():
    """En enkel rot-endepunkt som peker til dokumentasjonen."""
    return {"message": "ClubSite adminstruktur – se /docs for API-endepunkter og struktur"}

