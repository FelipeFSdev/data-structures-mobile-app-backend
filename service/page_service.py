from sqlmodel import select, Session
from model.page_model import Page
from schema.page_schema import PageIn


class PageService:
    def get_pages(self, session: Session, current_user: dict, title: str):
        if current_user is not None:
            pages = session.exec(select(Page).where(Page.title == title)).all()

            return pages

    def create_page(self, session: Session, body: PageIn):
        new_page = Page(
            title=body.title,
            content=body.content,
            image_url=body.image_url
        )
        session.add(new_page)
        session.commit()
        session.refresh(new_page)

        return None
