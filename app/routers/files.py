from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Form
from sqlmodel import Session, select

from app import log
from app.dependencies import get_session
from app.functions.files import write_file_to_disk, delete_file_from_disk
from app.models.metadata import Metadata

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
def create_file(session: SessionDep, content: str = Form(...), name: str = Form(...), category: str = Form(None), ) -> Metadata :
    """
    Permet de sauvegarder un nouveau fichier
    :param content: Texte de l'article
    :param session: Session de connexion à la base de données
    :param name: Nom du fichier
    :param category: Category du fichier
    :return: Les metadata du fichier ajouté
    """

    try:
        # Construction des metadata et ajout en base
        file = Metadata(name=name, category=category)
        session.add(file)

        # Ecriture du fichier sur le disk
        write_file_to_disk(content=content, name=name)

        # Commit avec la base
        session.commit()
        session.refresh(file)

        return file

    except Exception as e:
        log.error(f"Erreur lors de la sauvegarde du fichier : {e}")
        raise HTTPException(status_code=500, detail=e)

@router.delete("/delete/{metadata_id}")
def create_file(metadata_id: int, session: SessionDep):

    # Récupérer les metadata en base
    metadata = session.exec(select(Metadata).where(Metadata.id == metadata_id)).first()

    if not metadata:
        log.error(f"Metadata introuvables pour l'ID : [{metadata_id}")

    # Suppression des métadata en base
    session.delete(metadata)

    # Suppresion du fichier sur le disk
    delete_file_from_disk(name=metadata.name)

    session.commit()

    return {"message": f"Fichier avec ID {metadata_id} supprimé"}