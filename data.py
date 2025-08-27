from schemas import MenuLink, TableModel, TableRow, TableCell, PageModel

# Hovedmeny for admin
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
        ])
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
        ])
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
        ])
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
        ])
    ]
)

sidemal_page = PageModel(
    navn="Sidemal",
    url="/admin/template_sub",
    beskrivelse="Rediger og administrer sidemaler for ulike deler av nettstedet.",
    meny=main_menu,
    tabeller=[sidemal_tabell]
)
