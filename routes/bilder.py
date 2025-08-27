from fastapi import APIRouter
from schemas import PageModel
from data import bilder_page

router = APIRouter()


@router.get(
    "/bilder",
    response_model=PageModel,
    summary="Hent Bilder",
    tags=["Struktur"],
    responses={
        200: {
            "description": "Eksempel på PageModel for Bilder",
            "content": {"application/json": {"example": bilder_page.model_dump()}}
        }
    },
)
def hent_bilder():
    """Returnerer datastruktur og eksempeldata for Bilder-modulen."""
    return bilder_page
