from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import Depends

from sections.system.containers import DependencyInjectorCheckContainer
from sections.system.controllers import router
from sections.system.di_check.interfaces import DependencyInjectorCheckService
from sections.system.di_check.schemas import DependencyInjectorCheckResponse


@router.get("/di-check", response_model=DependencyInjectorCheckResponse)
@inject
async def di_check(
    service: DependencyInjectorCheckService = Depends(
        Provide[DependencyInjectorCheckContainer.di_check_service],
    ),
) -> DependencyInjectorCheckResponse:
    response = service.check()
    return response
