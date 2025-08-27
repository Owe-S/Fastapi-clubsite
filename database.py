import os
import urllib
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Read an ODBC string from .env (RAW, exactly as you’d use in a DSN)
# Example you can add to your .env (no URL-encoding here):
#
# READWRITE_ODBC_CONN="Driver={ODBC Driver 18 for SQL Server};Server=89.221.242.124,1433;Database=CS4-ORIGINAL;UID=owestest;PWD=hhdtR53rs6jDser5;Encrypt=yes;TrustServerCertificate=yes;Application Intent=ReadWrite;"
#
odbc_conn = os.getenv("READWRITE_ODBC_CONN", "")

if odbc_conn:
    # quote the entire ODBC string and let SQLAlchemy+pyodbc consume via odbc_connect
    params = urllib.parse.quote_plus(odbc_conn)
    DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
    connect_args = {}  # SQL Server does not need special args here
else:
    # dummy in‐memory fallback
    DATABASE_URL = "sqlite:///./clubsite.db"
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()