from utils.paths import APP_DESCRIPTION_PATH


def get_app_description() -> str:
    app_description = APP_DESCRIPTION_PATH.read_text(encoding="utf-8")
    return app_description


def get_version() -> str:
    return "0.1.0"
