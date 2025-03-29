from functools import cache
from pathlib import Path

from settings import EnvEnum

APP_ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DESCRIPTION_PATH = APP_ROOT_DIR / "description.md"
APP_DI_CONFIG_DIR = APP_ROOT_DIR / "configs"

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent
TESTS_DIR = PROJECT_ROOT_DIR / "tests"


@cache
def ENV_TO_DI_CONFIG_PATH(env: EnvEnum) -> Path:
    match env:
        case EnvEnum.LOCAL:
            return APP_DI_CONFIG_DIR / "local.yml"
        case EnvEnum.TEST:
            return APP_DI_CONFIG_DIR / "test.yml"
        case EnvEnum.DEV:
            return APP_DI_CONFIG_DIR / "dev.yml"
        case EnvEnum.STG:
            return APP_DI_CONFIG_DIR / "stg.yml"
        case EnvEnum.PROD:
            return APP_DI_CONFIG_DIR / "prod.yml"
        case _:
            raise ValueError("Not supported env value")
