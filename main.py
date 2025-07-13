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
    docs_url=None,     # disable default Swagger UI
    redoc_url=None,    # disable default ReDoc
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

from fastapi.responses import HTMLResponse

@app.get("/", include_in_schema=False)
async def api_index() -> HTMLResponse:
    """
    Simple HTML index page linking to /docs, /redoc and all GET routes.
    """
    links = [
        "<li><a href='/docs'>Swagger UI</a></li>",
        "<li><a href='/redoc'>ReDoc</a></li>"
    ]
    for route in app.routes:
        if "GET" not in route.methods or not route.include_in_schema:
            continue
        path = route.path
        if path in ("/openapi.json", "/docs", "/redoc"):
            continue
        links.append(f"<li><a href='{path}'>{path}</a></li>")

    html = f"""
    <html>
      <head><title>{app.title} – Index</title></head>
      <body>
        <h1>{app.title}</h1>
        <ul>
          {''.join(links)}
        </ul>
      </body>
    </html>
    """
    return HTMLResponse(html)

@app.get("/healthcheck", tags=["Health"])
def healthcheck(session: Session = Depends(get_session)):
    try:
        session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB feilet: {e}")

@app.get("/chat", tags=["Chat"], dependencies=[Depends(get_current_user)])
async def chat(q: str):
    reply = ask_chatgpt(q)
    return {"reply": reply}

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

@app.get("/redoc", include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} – ReDoc",
    )