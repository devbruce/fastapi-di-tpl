from pydantic import BaseModel


class DependencyInjectorCheckResponse(BaseModel):
    injected_config_value: str
