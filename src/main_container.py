from typing import Self

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Provider
from loguru import logger

from core.system.containers import SystemContainer
from utils.app_info import get_app_settings
from utils.paths import ENV_TO_DI_CONFIG_PATH

ENV = get_app_settings().ENV


class MainContainer(DeclarativeContainer):
    config = providers.Configuration(yaml_files=[str(ENV_TO_DI_CONFIG_PATH(ENV))])

    system_container: Provider[DeclarativeContainer] = providers.Container(
        SystemContainer,
        config=config.system,
    )

    @classmethod
    def create_wired_container(cls) -> Self:
        logger.info("* [START] Wiring dependency-injector containers")
        main_container = cls()
        for container in main_container.traverse(types=[providers.Container]):
            container.wire(packages=["core"])
        logger.info("* [COMPLETED] Wiring dependency-injector containers")
        return main_container
