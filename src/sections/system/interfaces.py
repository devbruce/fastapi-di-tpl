from abc import ABC
from abc import abstractmethod

from sections.system.schemas import DependencyInjectorCheckResponse


class DependencyInjectorCheckService(ABC):
    @abstractmethod
    def check(self) -> DependencyInjectorCheckResponse:
        pass
