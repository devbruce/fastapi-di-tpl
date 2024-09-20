from dependency_injector import containers
from dependency_injector import providers
from dependency_injector.providers import Provider

from core.system.di_check.containers import DependencyInjectorCheckContainer


class SystemContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_check_container: Provider[containers.DeclarativeContainer] = providers.Container(
        DependencyInjectorCheckContainer,
        config=config.di_check,
    )
