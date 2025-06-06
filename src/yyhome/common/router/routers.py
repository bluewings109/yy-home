from yyhome.adapter.inbound.api.elevator_api import router as elevator_router
from fastapi import APIRouter

router = APIRouter(prefix="/api/yyhome/v1", tags=["elevator"])

router.include_router(elevator_router)
