from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import RedirectResponse

from sections.system.di_containers import DependencyInjectorCheckContainer
from sections.system.interfaces import DependencyInjectorCheckService
from sections.system.schemas import DependencyInjectorCheckResponse
from sections.system.schemas import HealthResponse

router = APIRouter(tags=["System"])


@router.get("/", include_in_schema=False)
async def redirect_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="UP")


@router.get("/di-check", response_model=DependencyInjectorCheckResponse)
@inject
async def di_check(
    service: DependencyInjectorCheckService = Depends(
        Provide[DependencyInjectorCheckContainer.di_check_service],
    ),
) -> DependencyInjectorCheckResponse:
    response = service.check()
    return response
