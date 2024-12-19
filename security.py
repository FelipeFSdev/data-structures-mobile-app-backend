import jwt
import time
import cryptocode
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from settings import HASH_KEY, JWT_KEY, JWT_ALGORITHM
from jwt.exceptions import ExpiredSignatureError


def hash_password(password: str):
    hashed_pass = cryptocode.encrypt(password, HASH_KEY)
    return hashed_pass


def unhash_password(hashed_pass: str):
    password = cryptocode.decrypt(hashed_pass, HASH_KEY)
    return password


def get_token(name: str, email: str):
    payload = {
        "exp": time.time() + (30*60),
        "name": name,
        "email": email
    }
    token = jwt.encode(payload, JWT_KEY, JWT_ALGORITHM)

    return {"name": name, "token": token}


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_KEY, JWT_ALGORITHM)

        return decoded_token
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token."
        )


def get_current_user(
        token: Annotated[
            HTTPAuthorizationCredentials,
            Depends(HTTPBearer())]
):
    return decode_token(token.credentials)


def login_dependency(
        current_user: Annotated[dict, Depends(get_current_user)]
):
    return current_user
