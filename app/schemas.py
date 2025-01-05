from typing import Optional
from pydantic import BaseModel

class SewageBase(BaseModel):
    name: str
    description: Optional[str] = None
    flow_rate: float

class SewageCreate(SewageBase):
    pass

class Sewage(SewageBase):
    id: int

    class Config:
        from_attributes = True
