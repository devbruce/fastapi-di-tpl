import asyncio

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import ASGITransport
from httpx import AsyncClient

from main import create_app


@pytest.fixture(scope="session")
def app() -> FastAPI:
    app: FastAPI = create_app()
    return app


@pytest.fixture(scope="session")
def test_client(app: FastAPI) -> TestClient:
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="session")
def async_test_client(app: FastAPI) -> AsyncClient:
    transport = ASGITransport(app=app)
    async_test_client = AsyncClient(base_url="http://test", transport=transport)
    return async_test_client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
