# models.py
from sqlalchemy import (
    Column, Integer, Boolean, SmallInteger,
    DateTime, String, Text
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'News_Articles'

    articleID        = Column(Integer,      primary_key=True, index=True)
    depID            = Column(Integer,      nullable=False)
    boolPubl         = Column(Boolean,      nullable=False)
    boolShow         = Column(Boolean,      nullable=False)
    boolPri          = Column(Boolean,      nullable=False)
    template         = Column(SmallInteger, nullable=True)
    validfrom        = Column(DateTime,     nullable=False)
    validto          = Column(DateTime,     nullable=False)
    author           = Column(String(100),  nullable=True)
    heading          = Column(String(100),  nullable=False)
    urlTitle         = Column(String(200),  nullable=False)
    indexImageID     = Column(Integer,      nullable=True)
    indexImage       = Column(String(100),  nullable=True)
    indexImagePath   = Column(String(200),  nullable=True)
    indeximg_descr   = Column(String(500),  nullable=True)
    templateImageID  = Column(Integer,      nullable=True)
    templateImage    = Column(String(200),  nullable=True)
    templimg_descr   = Column(String(500),  nullable=True)
    ingress          = Column(String(1000), nullable=True)
    newscontent      = Column(Text,         nullable=True)
    pagedescription  = Column(String(500),  nullable=True)
    useFBcomments    = Column(Boolean,      nullable=True)
    date_published   = Column(DateTime,     nullable=True)
    date_created     = Column(DateTime,     nullable=False)
    created_by       = Column(String(100),  nullable=True)
    date_modified    = Column(DateTime,     nullable=True)
    modified_by      = Column(String(100),  nullable=True)
    amtReceivers     = Column(Integer,      nullable=True)
    videoUrl         = Column(String(200),  nullable=True)
    boolInfoscreen   = Column(Boolean,      nullable=True)
    boolBoxed        = Column(Boolean,      nullable=True)
    boolRss          = Column(Boolean,      nullable=True)
    boolToFacebook   = Column(Boolean,      nullable=True)
# models.py (legg nederst, etter NewsArticle)

from sqlalchemy import Column, Integer, String, Float, Boolean, CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SiteUser(Base):
    __tablename__ = "Siteusers"

    userID       = Column("userID", Integer, primary_key=True, index=True)
    oldID        = Column("oldID", Integer, nullable=True)
    memberID     = Column("memberID", String(20), nullable=True)
    gender       = Column("gender", CHAR(1), nullable=False)
    boolPrivate  = Column("boolPrivate", Boolean, nullable=False)
    userName     = Column("userName", String(50), nullable=True, unique=True, index=True)
    lastName     = Column("lastName", String(30), nullable=True)
    firstName    = Column("firstName", String(30), nullable=True)
    hcp          = Column("hcp", Float, nullable=True)
    email        = Column("email", String(50), nullable=True)
    pwdHash      = Column("pwdHash", String(40), nullable=True)
    telephone    = Column("telephone", String(20), nullable=True)
    regDate      = Column("regDate", DateTime, nullable=True)

