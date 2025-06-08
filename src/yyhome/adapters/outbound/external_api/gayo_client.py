from http import HTTPStatus
from logging import Logger

import requests

from yyhome.adapters.outbound.external_api.schemas.gayo_request import GayoElevatorCallRequest
from yyhome.adapters.outbound.external_api.schemas.gayo_request import GayoLoginRequest
from yyhome.adapters.outbound.external_api.schemas.gayo_response import (
    GayoLoginResponse,
)
from yyhome.application.auth.jwt_service import JWTService
from yyhome.config.logging_config import get_logger
from yyhome.config.settings import Settings
from yyhome.exceptions.http_status_exception import HTTPStatusException
from yyhome.ports.outbound.gayo_port import GayoPort


class GayoClient(GayoPort):
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self.token: str | None = None
        self.logger: Logger = get_logger(__name__)

    def refresh_token(self):
        login_url: str = self.settings.gayo_service_url + "/Login"
        login_request_body: GayoLoginRequest = GayoLoginRequest(phone_number=self.settings.gayo_phone_number)
        login_request_headers: dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": ""
        }
        try:
            response = requests.post(login_url, headers=login_request_headers, json=login_request_body.model_dump(by_alias=True)) # Body -> camelCase
        except requests.exceptions.RequestException as e:
            self.logger.error("Failed to login to Gayo")
            raise HTTPStatusException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Failed to login to Gayo") from e

        if 400 <= response.status_code < 600:
            self.logger.error("Login to Gayo failed.")
            raise HTTPStatusException(status_code=response.status_code, detail=f"Failed to login to Gayo. status_code={response.status_code}, response.text={response.text}")
        else:
            self.logger.info("Successfully Logged in to Gayo")

        login_response: GayoLoginResponse = GayoLoginResponse(**response.json())

        self.token = login_response.authorization.split("Bearer ")[1]

    def call_elevator(self):
        if JWTService.is_token_expired(self.token):
            self.refresh_token()

        elevator_call_url: str = self.settings.gayo_service_url + "/HomeElevatorCall"
        elevator_call_body: GayoElevatorCallRequest = GayoElevatorCallRequest(
            buil_dong=self.settings.dong,
            floor=self.settings.floor,
            buil_code=self.settings.building_code,
            line=self.settings.line,
            buil_ho=self.settings.ho,
        )

        elevator_call_headers: dict[str, str] = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "",
        }

        try:
            response = requests.post(elevator_call_url, headers=elevator_call_headers, json=elevator_call_body.model_dump()) # Body -> snake_case
        except requests.exceptions.RequestException as e:
            self.logger.error("Failed to call elevator")
            raise HTTPStatusException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Failed to call elevator") from e

        if 400 <= response.status_code < 600:
            self.logger.error("Elevator call failed.")
            raise HTTPStatusException(
                status_code=response.status_code,
                detail=f"Failed to call elevator. status_code={response.status_code}, response.text={response.text}",
            )
        else:
            self.logger.info("Successfully called elevator")
