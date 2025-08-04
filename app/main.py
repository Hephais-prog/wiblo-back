from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import create_db_and_tables
from app.routers.article import router as article
from app.routers.category import router as category

app = FastAPI(lifespan=create_db_and_tables)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(article)
app.include_router(category)


@app.get("/")
def read_root():
    return "Backend API for Wiblo !"