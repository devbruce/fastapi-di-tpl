from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import Depends

from core.system.containers import DependencyInjectorCheckContainer
from core.system.controllers import router
from core.system.di_check.interfaces import DependencyInjectorCheckService
from core.system.di_check.schemas import DependencyInjectorCheckResponse


@router.get("/di-check", response_model=DependencyInjectorCheckResponse)
@inject
async def di_check(
    service: DependencyInjectorCheckService = Depends(
        Provide[DependencyInjectorCheckContainer.di_check_service],
    ),
) -> DependencyInjectorCheckResponse:
    response = service.check()
    return response
