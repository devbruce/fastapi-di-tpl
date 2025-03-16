from enum import Enum

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class EnvEnum(str, Enum):
    LOCAL = "local"
    TEST = "test"
    DEV = "dev"
    STG = "stg"
    PROD = "prod"


class AppSettings(BaseSettings):
    ENV: EnvEnum = EnvEnum.LOCAL
    VERSION: str = "undefined"

    model_config = SettingsConfigDict(env_prefix="APP_")
