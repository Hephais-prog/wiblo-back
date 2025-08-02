from sqlmodel import Field, SQLModel


class Metadata(SQLModel, table=True):
    """
    Classe et table : metadata d'un article
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    category: str = Field(nullable=True, default=None, index=True)