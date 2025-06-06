import requests
from yyhome.adapters.outbound.external_api.schemas.gayo_request import GayoLoginRequest
from yyhome.ports.outbound.gayo_port import GayoPort


class GayoClient(GayoPort):
    def login(self, phone_number: str) -> str:
        login_request: GayoLoginRequest = GayoLoginRequest(phone_number=phone_number)
        requests.post()

    def call_elevator(
        self,
        building_code: str, # 아파트 코드
        line: str, # 라인
        dong: str, # 동
        floor: str, # 층
        ho: str # 호
    ):
        pass
