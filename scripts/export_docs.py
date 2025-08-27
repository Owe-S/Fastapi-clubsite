# filepath: scripts/export_docs.py
import os
import sys

# add project root (one level up) to module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from main import app
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

def main():
    os.makedirs("docs", exist_ok=True)

    # dump OpenAPI spec
    spec = app.openapi()
    with open("docs/openapi.json", "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)

    # standalone Swagger UI
    swagger = get_swagger_ui_html(openapi_url="openapi.json", title=f"{app.title} – Swagger UI")
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(swagger.body.decode())

    # standalone ReDoc
    redoc = get_redoc_html(openapi_url="openapi.json", title=f"{app.title} – ReDoc")
    with open("docs/redoc.html", "w", encoding="utf-8") as f:
        f.write(redoc.body.decode())

if __name__ == "__main__":
    main()