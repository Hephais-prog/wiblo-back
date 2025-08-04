import datetime
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from app.models.category import Category


class Article(SQLModel, table=True):
    """
    Classe et table : metadata d'un article
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    creation_datetime: datetime.datetime = Field(nullable=False, index=True)
    last_updated_datetime: datetime.datetime = Field(nullable=False, index=True)

    category_id: int | None = Field(default=None, foreign_key="category.id", ondelete="SET NULL")
    category: Category | None = Relationship(back_populates="articles")


class ArticleBase(BaseModel):
    name: str
    creation_datetime: datetime.datetime
    last_updated_datetime: datetime.datetime
    category_id: int

class ArticleCreate(ArticleBase):
    pass