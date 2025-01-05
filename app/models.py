from sqlmodel import SQLModel, Field
from typing import Optional

class Sewage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    flow_rate: float
