from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .database import engine, Base
from .endpoints import sewage
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sewage.router)

# Mount the static files directory
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

# Serve index.html as the default page
@app.get("/")
async def read_index():
    return FileResponse(os.path.join("ui", "index.html"))
