import pytest
import yaml
from fastapi import status
from httpx import AsyncClient

from settings import AppSettings
from utils.paths import ENV_TO_DI_CONFIG_PATH


@pytest.mark.e2e
async def test_redirect_docs(async_test_client: AsyncClient):
    response = await async_test_client.get("/")
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.is_redirect is True
    assert response.next_request.url.raw_path.decode() == "/docs"  # type: ignore


@pytest.mark.e2e
async def test_health(async_test_client: AsyncClient):
    response = await async_test_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "UP"


@pytest.mark.e2e
async def test_di_config_checker(async_test_client: AsyncClient, app_settings: AppSettings):
    config_text = ENV_TO_DI_CONFIG_PATH(app_settings.ENV).read_text(encoding="utf-8")
    config = yaml.safe_load(config_text)
    expected_injected_config_env = config["system"]["di_config_checker"]["env"]

    response = await async_test_client.get("/di-config-check")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["injected_config_env"] == expected_injected_config_env
