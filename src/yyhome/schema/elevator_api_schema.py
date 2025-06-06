from yyhome.schema.camel_case_base_model import CamelCaseBaseModel


class GayoLoginRequest(CamelCaseBaseModel):
    phone_number: str

class GayoLoginResponse(CamelCaseBaseModel):
    authorization: str
