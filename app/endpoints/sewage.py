from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_session

router = APIRouter()

@router.post("/sewages/", response_model=schemas.Sewage)
def create_sewage(sewage: schemas.SewageCreate, session: Session = Depends(get_session)):
    return crud.create_sewage(session, models.Sewage.from_orm(sewage))

@router.get("/sewages/", response_model=List[schemas.Sewage])
def read_sewages(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return crud.get_sewages(session, skip=skip, limit=limit)

@router.get("/sewages/{sewage_id}", response_model=schemas.Sewage)
def read_sewage(sewage_id: int, session: Session = Depends(get_session)):
    db_sewage = crud.get_sewage(session, sewage_id=sewage_id)
    if db_sewage is None:
        raise HTTPException(status_code=404, detail="Sewage not found")
    return db_sewage
