from typing import Annotated
from fastapi import APIRouter, Depends
from database.session import SessionDep
from service.page_service import PageService
from view.page_view import PageOut
from schema.page_schema import PageIn
from security import login_dependency

router = APIRouter(prefix="/page", dependencies=[Depends(login_dependency)])
service = PageService()


@router.get("/{title}", response_model=list[PageOut])
def get_pages(
        session: SessionDep,
        current_user: Annotated[dict[str, str], Depends(login_dependency)],
        title: str
):
    return service.get_pages(session, current_user, title)


@router.post("/create", status_code=204)
def create_page(session: SessionDep, body: PageIn):
    return service.create_page(session, body)
