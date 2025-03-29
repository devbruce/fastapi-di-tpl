from dependency_injector import containers
from dependency_injector import providers
from dependency_injector.providers import Provider

from core.system.di_config_checker.containers import DependencyInjectorConfigCheckerContainer


class SystemContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_config_checker_container: Provider[containers.DeclarativeContainer] = providers.Container(
        DependencyInjectorConfigCheckerContainer,
        config=config.di_config_checker,
    )
