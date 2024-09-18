from dependency_injector import containers
from dependency_injector import providers
from dependency_injector.providers import Provider

from sections.system.interfaces import DependencyInjectorCheckService
from sections.system.services import DependencyInjectorCheckServiceImpl


class DependencyInjectorCheckContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_check_service: Provider[DependencyInjectorCheckService] = providers.Singleton(
        DependencyInjectorCheckServiceImpl,
        injected_config_value=config.value,
    )


class SystemContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_check_container: Provider[containers.DeclarativeContainer] = providers.Container(
        DependencyInjectorCheckContainer,
        config=config.di_check,
    )
