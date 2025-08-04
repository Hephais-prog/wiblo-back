from typing import Annotated, Sequence
from fastapi import Depends, APIRouter, HTTPException, status
from sqlmodel import Session, select

from app import log
from app.dependencies import get_session
from app.models.article import Article, ArticleCreate

router = APIRouter(
    prefix="/article",
    tags=["article"],
    responses={
        404: {
            "description": "Not found"
        }
    },
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.get('/articles')
def get_all_artcile(session: SessionDep) -> Sequence[Article]:
    """
    Fonction permettant de récupérer tous les articles
    :param session:
    :return:
    """

    articles = session.exec(select(Article)).all()
    return articles

@router.get('/')
def get_all_artcile(session: SessionDep, article_id: int) -> Sequence[Article]:
    """
    Fonction permettant de récupérer un article gràce à son ID
    :param session:
    :param article_id:
    :return:
    """

    article = session.exec(select(Article).where(Article.id == article_id)).first()
    return article

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_article(session: SessionDep, article: ArticleCreate) -> Article :
    """
    Permet de sauvegarder un nouveau fichier
    :param session: Session de connexion à la base de données
    :param article: article à créer
    :return: L'article ajouté
    """

    try:
        article = Article(**article.model_dump())
        session.add(article)
        session.commit()
        session.refresh(article)

        return article

    except Exception as e:
        log.error(f"Erreur lors de la sauvegarde du fichier : {e}")
        raise HTTPException(status_code=500, detail=e)

@router.delete("/")
def delete_article(session: SessionDep, article_id: int):

    article = session.exec(select(Article).where(Article.id == article_id)).first()

    if article:
        session.delete(article)
        session.commit()

    return article