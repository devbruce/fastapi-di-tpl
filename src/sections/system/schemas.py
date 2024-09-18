from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["UP", "DOWN"]


class DependencyInjectorCheckResponse(BaseModel):
    injected_config_value: str
