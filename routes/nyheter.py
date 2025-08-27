from fastapi import APIRouter
from schemas import PageModel
from data import nyheter_page

router = APIRouter()


@router.get(
    "/nyheter",
    response_model=PageModel,
    summary="Hent Nyheter",
    tags=["Struktur"],
    responses={
        200: {
            "description": "Eksempel på PageModel for Nyheter",
            "content": {"application/json": {"example": nyheter_page.model_dump()}}
        }
    },
)
def hent_nyheter():
    """Returnerer datastruktur og eksempeldata for Nyheter-modulen."""
    return nyheter_page
