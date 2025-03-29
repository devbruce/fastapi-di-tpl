from dependency_injector import containers
from dependency_injector import providers
from dependency_injector.providers import Provider

from core.system.di_config_checker.interfaces import DependencyInjectorConfigChecker
from core.system.di_config_checker.services import DependencyInjectorConfigCheckerSimpleImpl


class DependencyInjectorConfigCheckerContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    di_config_checker: Provider[DependencyInjectorConfigChecker] = providers.Singleton(
        DependencyInjectorConfigCheckerSimpleImpl,
        injected_config_env=config.env,
    )
