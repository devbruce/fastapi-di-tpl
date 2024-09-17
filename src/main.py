from contextlib import asynccontextmanager

from fastapi import FastAPI

from utils.app_info import get_app_description
from utils.app_info import get_version


def create_app() -> FastAPI:
    from sections.system.controllers import router as system_router

    app = FastAPI(
        title="FastAPI with Dependency Injector",
        description=get_app_description(),
        version=get_version(),
        lifespan=lifespan,
    )

    # Routers
    app.include_router(system_router)

    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on_event: startup

    yield

    # on_event: shutdown
