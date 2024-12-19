from pydantic import BaseModel


class PageOut(BaseModel):
    title: str
    content: str
    image_url: str | None
