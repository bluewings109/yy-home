from yyhome.common.camel_case_base_model import CamelCaseBaseModel


class GayoLoginRequest(CamelCaseBaseModel):
    phone_number: str

class GayoElevatorCallRequest(CamelCaseBaseModel):
    buil_dong: str
    floor: str
    buil_code: str
    line: str
    buil_ho: str
