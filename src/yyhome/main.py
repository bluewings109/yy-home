import uvicorn
from fastapi import FastAPI

from yyhome.adapters.inbound.http.routers.v1.elevator_router import (
    router as v1_elevator_router,
)
from yyhome.config.settings import Settings
from yyhome.di_container import DIContainer
from yyhome.exceptions.http_status_exception import HTTPStatusException
from yyhome.middleware.exception_handler import http_status_exception_handler

di_container = DIContainer()
di_container.wire()

settings: Settings = DIContainer.settings()
app = FastAPI(
    title="YY Home App",
    description="YY Home App",
    version="1.0.0",
    docs_url=settings.docs_url,
)


app.include_router(v1_elevator_router, prefix="/api/v1/elevator", tags=["elevator router v1"])

app.add_exception_handler(HTTPStatusException, http_status_exception_handler)

di_container = DIContainer()
di_container.wire()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
