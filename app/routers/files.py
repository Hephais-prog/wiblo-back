from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session

from app.dependencies import get_session
from app.models.files import File

router = APIRouter(
    prefix="/files",
    tags=["files"],
    responses={
        404: {
            "description": "Not found"
        }
    },
)

SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/add/")
def create_file(hero: File, session: SessionDep) -> File:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@router.get("/get_by_id/{hero_id}")
def get_file_by_id(file_id: int, session: SessionDep) -> File:
    file = session.get(File, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file