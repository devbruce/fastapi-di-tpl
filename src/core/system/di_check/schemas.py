from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.config import JsonDict

from core.system.di_check.examples import response_examples


class DependencyInjectorCheckResponse(BaseModel):
    injected_config_value: str

    model_config = ConfigDict(
        json_schema_extra=cast(
            JsonDict,
            {
                "examples": response_examples,
            },
        )
    )
