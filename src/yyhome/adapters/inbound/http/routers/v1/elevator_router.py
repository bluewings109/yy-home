from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide
from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import JSONResponse

from yyhome.adapters.inbound.http.routers.v1.schemas.elevator_response import ElevatorCallResponse
from yyhome.di_container import DIContainer
from yyhome.ports.inbound.elevator_port import ElevatorPort

router = APIRouter()


@router.post(
    "/call",
    description="엘리베이터 호출",
    response_class=JSONResponse,
)
@inject
def call_elevator(
    elevator_port: Annotated[ElevatorPort, Depends(Provide[DIContainer.elevator_service])]
):
    elevator_port.call_elevator()
    return ElevatorCallResponse(status="success")
