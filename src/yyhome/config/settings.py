from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    docs_url: str

    # For Gayo Service
    gayo_service_url: str
    gayo_phone_number: str
    building_code: str # 아파트 코드
    line: str # 라인
    dong: str # 동
    floor: str # 층
    ho: str # 호


    model_config = {
        "env_file": f".env.{os.getenv("PROFILE").lower()}" if os.getenv("PROFILE") else None, # pyright: ignore [reportOptionalMemberAccess]
    }

