from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import Depends

from core.system.containers import DependencyInjectorConfigCheckerContainer
from core.system.controllers import router
from core.system.di_config_checker.interfaces import DependencyInjectorConfigChecker
from core.system.di_config_checker.schemas import DependencyInjectorConfigCheckerResponse


@router.get("/di-config-check", response_model=DependencyInjectorConfigCheckerResponse)
@inject
async def di_check(
    service: DependencyInjectorConfigChecker = Depends(
        Provide[DependencyInjectorConfigCheckerContainer.di_config_checker],
    ),
) -> DependencyInjectorConfigCheckerResponse:
    response = service.check()
    return response
