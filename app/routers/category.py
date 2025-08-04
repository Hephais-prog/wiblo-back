from typing import Annotated, Sequence
from fastapi import Depends, APIRouter, HTTPException, status
from sqlmodel import Session, select

from app import log
from app.dependencies import get_session
from app.models.category import Category, CategoryCreate

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={
        404: {
            "description": "Not found"
        }
    },
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.get('/')
def get_all_categories(session: SessionDep) -> Sequence[Category]:
    """
    Fonction permettant de récupérer toutes les categories
    :param session:
    :return:
    """

    categories = session.exec(select(Category)).all()
    return categories

@router.get('/articles')
def get_all_articles(session: SessionDep, category_id: int) -> Sequence[Category]:
    """
    Fonction qui permet de récupérer la liste de tous les articles pour une catégorie
    :param session:
    :param category_id
    :return:
    """

    category = session.exec(select(Category).where(Category.id == category_id)).first()
    if category:
        return category.articles
    else:
        return []


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_category(session: SessionDep, category: CategoryCreate) -> Category:
    """
    Permet de créer une nouvelle catégorie
    :param session: Session de connexion à la base de données
    :param category: categories à créer
    :return: La catégorie ajoutée
    """

    try:
        category = Category(**category.model_dump())
        session.add(category)
        session.commit()
        session.refresh(category)

        return category

    except Exception as e:
        log.error(f"Erreur lors de la sauvegarde de la catégorie : {e}")
        raise HTTPException(status_code=500, detail=e)


@router.delete("/")
def delete_category(session: SessionDep, category_id: int):
    category = session.exec(select(Category).where(Category.id == category_id)).first()

    if category:
        session.delete(category)
        session.commit()

    return category