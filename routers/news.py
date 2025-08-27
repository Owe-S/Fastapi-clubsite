from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_session
from auth import get_current_user
from models import NewsArticle
from schemas import NewsArticleIn, NewsArticleOut

router = APIRouter(
    prefix="/news",
    tags=["Nyheter"],
    dependencies=[Depends(get_current_user)]
)

@router.get(
    "/",
    response_model=List[NewsArticleOut],
    operation_id="list_news"
)
def list_news(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    stmt = select(NewsArticle).offset(skip).limit(limit)
    return session.execute(stmt).scalars().all()

@router.post(
    "/",
    response_model=NewsArticleOut,
    status_code=201,
    operation_id="create_news"
)
def create_news(
    data: NewsArticleIn,
    current_user = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    now = datetime.utcnow()
    new_article = NewsArticle(
        **data.dict(),
        date_created=now,
        created_by=current_user.userName
    )
    session.add(new_article)
    session.commit()
    session.refresh(new_article)
    return new_article

@router.get(
    "/{article_id}",
    response_model=NewsArticleOut,
    operation_id="get_news"
)
def get_news(
    article_id: int,
    session: Session = Depends(get_session)
):
    article = session.get(NewsArticle, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="News not found")
    return article

@router.put(
    "/{article_id}",
    response_model=NewsArticleOut,
    operation_id="update_news"
)
def update_news(
    article_id: int,
    data: NewsArticleIn,
    current_user = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    article = session.get(NewsArticle, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="News not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(article, field, value)
    article.date_modified = datetime.utcnow()
    article.modified_by = current_user.userName
    session.commit()
    session.refresh(article)
    return article

@router.delete(
    "/{article_id}",
    status_code=204,
    operation_id="delete_news"
)
def delete_news(
    article_id: int,
    session: Session = Depends(get_session)
):
    article = session.get(NewsArticle, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="News not found")
    session.delete(article)
    session.commit()