from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.config import JsonDict

from core.system.di_config_checker.examples import response_examples


class DependencyInjectorConfigCheckerResponse(BaseModel):
    injected_config_env: str

    model_config = ConfigDict(
        json_schema_extra=cast(
            JsonDict,
            {
                "examples": response_examples,
            },
        )
    )
