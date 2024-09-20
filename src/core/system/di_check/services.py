from typing import override

from core.system.di_check.interfaces import DependencyInjectorCheckService
from core.system.di_check.schemas import DependencyInjectorCheckResponse


class DependencyInjectorCheckServiceImpl(DependencyInjectorCheckService):
    def __init__(self, injected_config_value: str):
        self.injected_config_value = injected_config_value

    @override
    def check(self) -> DependencyInjectorCheckResponse:
        response = DependencyInjectorCheckResponse(injected_config_value=self.injected_config_value)
        return response
