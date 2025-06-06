from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class CamelCaseBaseModel(BaseModel):
    model_config = {
        "populate_by_name": True,
        "alias_generator": to_camel,
    }