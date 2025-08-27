from pydantic import BaseModel, Field
from typing import List, Optional, Any


class TableCell(BaseModel):
    tekst: Optional[str] = Field(None, example="Eksempel tekst")
    href: Optional[str] = Field(None, example="/path/to/resource")
    type: Optional[str] = Field(None, example="tekst")
    placeholder: Optional[str] = Field(None, example="Placeholder")
    funksjon: Optional[str] = Field(None, example="Vis/Slett")


class TableRow(BaseModel):
    celler: List[TableCell]


class TableModel(BaseModel):
    url: str = Field(..., example="https://skigk.no/csadmin/news")
    kolonner: List[str] = Field(..., example=["ID", "Tittel", "Forfatter"])
    rader: List[TableRow]


class MenuLink(BaseModel):
    navn: str = Field(..., example="Nyheter")
    url: str = Field(..., example="/admin/news")
    ikoner: Optional[List[str]] = Field(None, example=["icon-news"])
    underpunkter: Optional[List['MenuLink']] = None


MenuLink.update_forward_refs()


class PageModel(BaseModel):
    navn: str = Field(..., example="Nyheter")
    url: str = Field(..., example="/admin/news")
    beskrivelse: Optional[str] = Field(None, example="Beskrivelse av modulen")
    meny: List[MenuLink]
    tabeller: List[TableModel]

    model_config = {
        "json_schema_extra": {
            "example": {
                "navn": "Nyheter",
                "url": "/admin/news",
                "beskrivelse": "Modul for å publisere og administrere nyhetsartikler.",
                "meny": [{"navn": "Nyheter", "url": "/admin/news"}],
                "tabeller": [
                    {
                        "url": "https://skigk.no/csadmin/news",
                        "kolonner": ["ID", "Tittel", "Forfatter"],
                        "rader": [
                            {"celler": [{"tekst": "1", "type": "int"}, {"tekst": "Tittel..."}]}
                        ],
                    }
                ],
            }
        }
    }
