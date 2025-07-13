# routers/activities.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from database import get_session
from auth import get_current_user
from models import Activities, Activities_DateTime
from schemas import ActivitiesIn, ActivitiesOut, ActivitiesDateTimeIn, ActivitiesDateTimeOut

router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/", response_model=List[ActivitiesOut], operation_id="list_activities")
def list_activities(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 10,
    date_from: Optional[datetime] = None,
    date_to: Optional[datetime] = None,
):
    """
    Hent en liste over aktiviteter.
    - **skip**: antall rader å hoppe over
    - **limit**: maks antall rader som returneres
    - **date_from**, **date_to**: filter på date_start mellom disse
    """
    stmt = (
        select(Activities)
        .where(Activities.boolShow == True)
        .order_by(Activities.date_start.desc())
    )
    if date_from:
        stmt = stmt.where(Activities.date_start >= date_from)
    if date_to:
        stmt = stmt.where(Activities.date_start <= date_to)
    stmt = stmt.offset(skip).limit(limit)
    results = session.execute(stmt).scalars().all()
    return results

@router.post("/", response_model=ActivitiesOut, operation_id="create_activity")
def create_activity(
    data: ActivitiesIn,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Opprett en ny aktivitet.
    """
    now = datetime.utcnow()
    new_act = Activities(
        **data.dict(),
        date_created=now,
        created_by=current_user.userName
    )
    session.add(new_act)
    session.commit()
    session.refresh(new_act)
    return new_act

@router.put("/{activity_id}", response_model=ActivitiesOut, operation_id="update_activity")
def update_activity(
    activity_id: int,
    data: ActivitiesIn,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Oppdater en eksisterende aktivitet.
    """
    stmt = select(Activities).where(Activities.activityID == activity_id)
    activity = session.execute(stmt).scalar_one_or_none()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity ikke funnet")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(activity, field, value)
    session.commit()
    session.refresh(activity)
    return activity

@router.delete("/{activity_id}", status_code=204, operation_id="delete_activity")
def delete_activity(
    activity_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Slett en aktivitet basert på ID.
    """
    stmt = select(Activities).where(Activities.activityID == activity_id)
    activity = session.execute(stmt).scalar_one_or_none()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity ikke funnet")
    session.delete(activity)
    session.commit()

# --- DateTime-endepunkter ---

@router.get("/{activity_id}/datetimes", response_model=List[ActivitiesDateTimeOut], operation_id="list_datetimes")
def list_datetimes(
    activity_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Hent alle datetime-poster for en aktivitet.
    """
    stmt = select(Activities_DateTime).where(Activities_DateTime.activityID == activity_id)
    return session.execute(stmt).scalars().all()

@router.post("/{activity_id}/datetimes", response_model=ActivitiesDateTimeOut, operation_id="create_datetime")
def create_datetime(
    activity_id: int,
    data: ActivitiesDateTimeIn,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Opprett en datetime-post for en aktivitet.
    """
    new_dt = Activities_DateTime(**data.dict())
    session.add(new_dt)
    session.commit()
    session.refresh(new_dt)
    return new_dt

@router.put("/datetimes/{dt_id}", response_model=ActivitiesDateTimeOut, operation_id="update_datetime")
def update_datetime(
    dt_id: int,
    data: ActivitiesDateTimeIn,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Oppdater en datetime-post basert på ID.
    """
    stmt = select(Activities_DateTime).where(Activities_DateTime.id == dt_id)
    record = session.execute(stmt).scalar_one_or_none()
    if not record:
        raise HTTPException(status_code=404, detail="DateTime post ikke funnet")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(record, field, value)
    session.commit()
    session.refresh(record)
    return record

@router.delete("/datetimes/{dt_id}", status_code=204, operation_id="delete_datetime")
def delete_datetime(
    dt_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    """
    Slett en datetime-post basert på ID.
    """
    stmt = select(Activities_DateTime).where(Activities_DateTime.id == dt_id)
    record = session.execute(stmt).scalar_one_or_none()
    if not record:
        raise HTTPException(status_code=404, detail="DateTime post ikke funnet")
    session.delete(record)
    session.commit()
