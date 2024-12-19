from fastapi import HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from schema.user_schema import UserIn
from model.user_model import User
from security import hash_password


class UserService:
    def create_user(self, session: Session, body: UserIn):
        try:
            user_pass = hash_password(body.password)
            new_user = User(
                name=body.name,
                email=body.email,
                password=user_pass
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            raise HTTPException(status_code=201)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already exists.")
