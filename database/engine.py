from model import page_model, user_model
from sqlmodel import create_engine, SQLModel
from settings import DB_URL, POSTGRES_URL

engine = create_engine(POSTGRES_URL, echo=True)


def get_engine():
    SQLModel.metadata.create_all(engine)
