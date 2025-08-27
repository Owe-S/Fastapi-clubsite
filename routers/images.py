from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime
import os, shutil

from database import get_session
from auth import get_current_user
from models import Images, Images_Categories
from schemas import ImageIn, ImageOut, ImageCategoryIn, ImageCategoryOut

router = APIRouter(
    prefix="/images",
    tags=["Images"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/", response_model=List[ImageOut], operation_id="list_images")
def list_images(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    stmt = select(Images).offset(skip).limit(limit)
    return session.execute(stmt).scalars().all()

@router.post("/", response_model=ImageOut, status_code=201, operation_id="create_image")
def create_image(
    data: ImageIn,
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    now = datetime.utcnow()
    # save file
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    filename = f"{int(now.timestamp())}_{file.filename}"
    path = os.path.join(upload_dir, filename)
    with open(path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    img = Images(**data.dict(), imagefile=filename, date_created=now, created_by=current_user.userName)
    session.add(img)
    session.commit()
    session.refresh(img)
    return img

@router.get("/{image_id}", response_model=ImageOut, operation_id="get_image")
def get_image(image_id: int, session: Session = Depends(get_session)):
    img = session.get(Images, image_id)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    return img

@router.put("/{image_id}", response_model=ImageOut, operation_id="update_image")
def update_image(image_id: int, data: ImageIn, session: Session = Depends(get_session)):
    img = session.get(Images, image_id)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    for k, v in data.dict(exclude_unset=True).items():
        setattr(img, k, v)
    session.commit()
    session.refresh(img)
    return img

@router.delete("/{image_id}", status_code=204, operation_id="delete_image")
def delete_image(image_id: int, session: Session = Depends(get_session)):
    img = session.get(Images, image_id)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    session.delete(img)
    session.commit()

# Simple category endpoints
@router.get("/categories", response_model=List[ImageCategoryOut], operation_id="list_categories")
def list_categories(session: Session = Depends(get_session)):
    stmt = select(Images_Categories)
    return session.execute(stmt).scalars().all()

@router.post("/categories", response_model=ImageCategoryOut, status_code=201, operation_id="create_category")
def create_category(data: ImageCategoryIn, session: Session = Depends(get_session)):
    cat = Images_Categories(**data.dict())
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat