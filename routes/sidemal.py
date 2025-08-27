from fastapi import APIRouter
from schemas import PageModel
from data import sidemal_page

router = APIRouter()


@router.get(
    "/sidemal",
    response_model=PageModel,
    summary="Hent Sidemal",
    tags=["Struktur"],
    responses={
        200: {
            "description": "Eksempel på PageModel for Sidemal",
            "content": {"application/json": {"example": sidemal_page.model_dump()}}
        }
    },
)
def hent_sidemal():
    """Returnerer datastruktur og eksempeldata for Sidemal-modulen."""
    return sidemal_page
