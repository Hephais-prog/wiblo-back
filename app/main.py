from fastapi import FastAPI

from app.dependencies import create_db_and_tables, get_session
from app.routers.files import router as router_files

app = FastAPI(lifespan=create_db_and_tables)

app.include_router(router_files)

@app.get("/")
def read_root():
    return "Backend API for Wiblo !"