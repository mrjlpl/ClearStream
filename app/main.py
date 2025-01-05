from fastapi import FastAPI
from .database import engine, Base
from .endpoints import sewage

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sewage.router)
