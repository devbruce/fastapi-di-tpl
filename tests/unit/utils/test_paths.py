from pathlib import Path

import pytest

from settings import EnvEnum
from utils.paths import APP_DI_CONFIG_DIR
from utils.paths import ENV_TO_DI_CONFIG_PATH


@pytest.mark.unit
@pytest.mark.parametrize(
    "env, expected",
    [
        (EnvEnum.LOCAL, APP_DI_CONFIG_DIR / "local.yml"),
        (EnvEnum.TEST, APP_DI_CONFIG_DIR / "test.yml"),
        (EnvEnum.DEV, APP_DI_CONFIG_DIR / "dev.yml"),
        (EnvEnum.STG, APP_DI_CONFIG_DIR / "stg.yml"),
        (EnvEnum.PRD, APP_DI_CONFIG_DIR / "prd.yml"),
    ],
)
def test_env_to_di_config_path(env: EnvEnum, expected: Path):
    result = ENV_TO_DI_CONFIG_PATH(env)
    assert result == expected
