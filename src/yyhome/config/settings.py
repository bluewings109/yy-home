from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    gayo_service_url: str


    model_config = {
        "env_file": f".env.{os.getenv("PROFILE").lower()}" if os.getenv("PROFILE") else None, # pyright: ignore [reportOptionalMemberAccess]
    }

