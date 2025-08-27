from fastapi import APIRouter
from schemas import PageModel
from data import dokumenter_page

router = APIRouter()


@router.get(
    "/dokumenter",
    response_model=PageModel,
    summary="Hent Dokumenter",
    tags=["Struktur"],
    responses={
        200: {
            "description": "Eksempel på PageModel for Dokumenter",
            "content": {"application/json": {"example": dokumenter_page.model_dump()}}
        }
    },
)
def hent_dokumenter():
    """Returnerer datastruktur og eksempeldata for Dokumenter-modulen."""
    return dokumenter_page
