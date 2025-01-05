from sqlmodel import Session, select
from .models import Sewage

def get_sewage(session: Session, sewage_id: int):
    return session.get(Sewage, sewage_id)

def create_sewage(session: Session, sewage: Sewage):
    session.add(sewage)
    session.commit()
    session.refresh(sewage)
    return sewage

def get_sewages(session: Session, skip: int = 0, limit: int = 10):
    return session.exec(select(Sewage).offset(skip).limit(limit)).all()
