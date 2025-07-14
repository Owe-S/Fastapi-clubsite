from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import timedelta
import inspect
import logging
import schemas
from sqlalchemy import inspect as sa_inspect    # ← add this

from database import get_session, Base, engine
from models import (
    SiteUser,
    NewsArticle,
    Activities,
    ActivitiesDateTime,
    Images,
    Images_Categories,
)
from auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from schemas import (
    Token,
    NewsArticleIn,
    NewsArticleOut,
    ActivitiesIn,
    ActivitiesOut,
    ActivitiesDateTimeIn,
    ActivitiesDateTimeOut,
    ImageIn,
    ImageOut,
    ImageCategoryIn,
    ImageCategoryOut,
)
from chatgpt_client import ask_chatgpt
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html, get_redoc_html
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="ClubSite Admin Struktur API",
    openapi_url="/openapi.json",
    docs_url=None,      # lar oss styre swagger‐UI manuelt
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for quick-and-dirty
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token", response_model=Token, tags=["Auth"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        data={"sub": user.userName}, 
        expires_delta=expires
    )
    return {"access_token": token, "token_type": "bearer"}

# ---- fjern ALT av denne duplikaten ----
# @app.get("/", include_in_schema=False)
# async def api_index() -> HTMLResponse:
#     …

# --- la kun én root‐endpoint stå igjen: meny for dokumentasjon ---
@app.get("/", include_in_schema=False)
async def docs_index() -> HTMLResponse:
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <title>API Documentation Index</title>
      </head>
      <body>
        <h1>API Documentation</h1>
        <ul>
          <li><a href="/docs">Swagger UI</a></li>
          <li><a href="/redoc">ReDoc</a></li>
          <li><a href="/openapi.json">OpenAPI JSON</a></li>
        </ul>
      </body>
    </html>
    """)

# dynamisk Swagger‐UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} – Swagger UI",
        swagger_ui_parameters={
            "docExpansion": "none",
            "tagsSorter": "alpha",
            "operationsSorter": "alpha",
        },
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_oauth2_redirect() -> HTMLResponse:
    return get_swagger_ui_oauth2_redirect_html()

# dynamisk ReDoc
@app.get("/redoc", include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} – ReDoc",
    )

# initialize basic logger for console output
logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.info("🔍 Auto-wiring models → CRUD routers…")

# Dynamically register CRUD for every model–schema pair
for name, model in inspect.getmembers(__import__("models"), inspect.isclass):
    if not hasattr(model, "__tablename__"):
        logging.debug(f"• Skipping {name}: no __tablename__")
        continue

    has_in  = hasattr(schemas, f"{name}In")
    has_out = hasattr(schemas, f"{name}Out")
    if not (has_in and has_out):
        logging.warning(f"• Skipping {name}: missing schemas {name}In/Out")
        continue

    # quick mapping check
    try:
        sa_inspect(model)
    except Exception as err:
        logging.error(f"• Skipping {name}: mapping error → {err}")
        continue

    prefix = model.__tablename__.lower()
    tag    = prefix.capitalize()
    logging.info(f"• Registering CRUD for {name} at /{prefix}")

    app.include_router(
        SQLAlchemyCRUDRouter(
            db_model      = model,
            db            = get_session,
            prefix        = prefix,
            tags          = [tag],
            schema        = getattr(schemas, f"{name}Out"),
            create_schema = getattr(schemas, f"{name}In"),
            dependencies  = [Depends(get_current_user)],
        )
    )