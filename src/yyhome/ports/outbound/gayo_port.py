from abc import ABC, abstractmethod

class GayoPort(ABC):

    @abstractmethod
    def login(self, phone_number: str) -> str:
        pass

    @abstractmethod
    def call_elevator(
        self,
        building_code: str, # 아파트 코드
        line: str, # 라인
        dong: str, # 동
        floor: str, # 층
        ho: str # 호
    ):
        pass
