from typing import TYPE_CHECKING
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from app.models.article import Article

class Category(SQLModel, table=True):
    """
    Classe et table : Catégorie pour regrouper les différents articles
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    description: str = Field(nullable=True, default=None, index=True)

    articles: list['Article'] = Relationship(back_populates="category")


class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass