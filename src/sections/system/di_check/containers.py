from dependency_injector import containers
from dependency_injector import providers
from dependency_injector.providers import Provider

from sections.system.di_check.interfaces import DependencyInjectorCheckService
from sections.system.di_check.services import DependencyInjectorCheckServiceImpl


class DependencyInjectorCheckContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_check_service: Provider[DependencyInjectorCheckService] = providers.Singleton(
        DependencyInjectorCheckServiceImpl,
        injected_config_value=config.value,
    )
