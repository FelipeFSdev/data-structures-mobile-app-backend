from pydantic import BaseModel


class PageIn(BaseModel):
    title: str
    content: str
    image_url: str | None = None
