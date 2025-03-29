from typing import override

from core.system.di_config_checker.interfaces import DependencyInjectorConfigChecker
from core.system.di_config_checker.schemas import DependencyInjectorConfigCheckerResponse


class DependencyInjectorConfigCheckerSimpleImpl(DependencyInjectorConfigChecker):
    def __init__(self, injected_config_env: str):
        self.injected_config_env = injected_config_env

    @override
    def check(self) -> DependencyInjectorConfigCheckerResponse:
        response = DependencyInjectorConfigCheckerResponse(injected_config_env=self.injected_config_env)
        return response
