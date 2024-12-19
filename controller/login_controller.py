from fastapi import APIRouter
from service.login_service import LoginService
from schema.login_schema import LoginIn
from view.login_view import LoginOut
from database.session import SessionDep

service = LoginService()
router = APIRouter(prefix="/login")


@router.post("/", response_model=LoginOut)
def get_auth(session: SessionDep, body: LoginIn):
    return service.get_auth(session, body)
