from functools import cache

from settings import AppSettings
from utils.paths import APP_DESCRIPTION_PATH


@cache
def get_app_settings() -> AppSettings:
    return AppSettings()


def get_app_description() -> str:
    app_description = APP_DESCRIPTION_PATH.read_text(encoding="utf-8")
    return app_description


def get_app_version() -> str:
    settings = get_app_settings()
    version = f"{settings.VERSION}:{settings.ENV.value}"
    return version
