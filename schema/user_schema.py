from pydantic import BaseModel


class UserIn(BaseModel):
    name: str | None = None
    email: str
    password: str
