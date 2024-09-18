from abc import ABC
from abc import abstractmethod

from sections.system.di_check.schemas import DependencyInjectorCheckResponse


class DependencyInjectorCheckService(ABC):
    @abstractmethod
    def check(self) -> DependencyInjectorCheckResponse:
        pass
