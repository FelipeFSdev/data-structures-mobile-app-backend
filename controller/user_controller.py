from fastapi import APIRouter
from database.session import SessionDep
from schema.user_schema import UserIn
from service.user_service import UserService

service = UserService()
router = APIRouter(prefix="/user")


@router.post("/create")
def create_user(session: SessionDep, body: UserIn):
    return service.create_user(session, body)
