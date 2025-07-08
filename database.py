# database.py

import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# 1) Last inn miljøvariabler
load_dotenv()

DB_USER   = os.getenv("DB_USER")
DB_PASS   = os.getenv("DB_PASS")
DB_HOST   = os.getenv("DB_HOST")
DB_NAME   = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")

# 2) Lag full ODBC-connect-string med kryptering av og tillat usikrede certs
odbc_str = (
    f"DRIVER={DB_DRIVER};"
    f"SERVER={DB_HOST};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASS};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)
# URL-enkode
connect_str = urllib.parse.quote_plus(odbc_str)

# 3) Bruk odbc_connect for å være sikker på at alle attributter plukkes opp
DATABASE_URL = f"mssql+aioodbc:///?odbc_connect={connect_str}"

# 4) Opprett AsyncEngine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,   # sett True hvis du vil se SQL i logg
    future=True
)

# 5) Session-factory som injiseres i FastAPI
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
