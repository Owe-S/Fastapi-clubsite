from fastapi import APIRouter
from schemas import PageModel
from data import undersider_page

router = APIRouter()


@router.get(
    "/undersider",
    response_model=PageModel,
    summary="Hent Undersider",
    tags=["Struktur"],
    responses={
        200: {
            "description": "Eksempel på PageModel for Undersider",
            "content": {"application/json": {"example": undersider_page.model_dump()}}
        }
    },
)
def hent_undersider():
    """Returnerer datastruktur og eksempeldata for Undersider-modulen."""
    return undersider_page
