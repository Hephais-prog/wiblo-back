from sqlmodel import Field, SQLModel, Column, String


class File(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    category: str = Field(nullable=True, default=None, index=True)