from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.engine import get_engine
from controller import page_controller, user_controller, login_controller
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server's up")
    get_engine()
    yield
    print("Server's down")


app = FastAPI(lifespan=lifespan)
app.include_router(page_controller.router)
app.include_router(user_controller.router)
app.include_router(login_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
