from abc import ABC
from abc import abstractmethod

from core.system.di_config_checker.schemas import DependencyInjectorConfigCheckerResponse


class DependencyInjectorConfigChecker(ABC):
    @abstractmethod
    def check(self) -> DependencyInjectorConfigCheckerResponse:
        pass
