from fastapi import HTTPException
from sqlmodel import Session, select
from schema.login_schema import LoginIn
from model.user_model import User
from security import unhash_password, get_token


class LoginService:
    def get_auth(self, session: Session, body: LoginIn):
        try:
            user = session.exec(
                select(User)
                .where(User.email == body.email)
            ).one_or_none()
            unhashed_password = unhash_password(user.password)
            if body.password != unhashed_password:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid email or password."
                )
            token = get_token(user.name, user.email)

            return token
        except AttributeError:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )
