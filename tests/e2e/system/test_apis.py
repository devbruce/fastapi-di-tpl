import pytest
from fastapi import status
from httpx import AsyncClient


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
