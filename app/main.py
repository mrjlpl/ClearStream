from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from .database import engine, Base
from .endpoints import sewage
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sewage.router)

# Mount the static files directory
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="ui")

# Serve index.html as the default page
@app.get("/", response_class=FileResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
