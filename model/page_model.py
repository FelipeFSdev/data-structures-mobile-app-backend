import uuid
from sqlmodel import SQLModel, Field


class Page(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    image_url: str | None = Field(default=None)
