from contextlib import asynccontextmanager

from fastapi import FastAPI

from main_container import MainContainer
from utils.app_info import get_app_description
from utils.app_info import get_app_version


def create_app() -> FastAPI:
    from core.system.controllers import router as system_router

    app = FastAPI(
        title="FastAPI with Dependency Injector",
        description=get_app_description(),
        version=get_app_version(),
        lifespan=lifespan,
    )

    # Wiring Dependency Injector Containers
    app.container = MainContainer.create_wired_container()  # type: ignore

    # Routers
    app.include_router(system_router)

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on_event: startup

    yield

    # on_event: shutdown
