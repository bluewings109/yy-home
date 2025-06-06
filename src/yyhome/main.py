import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from yyhome.adapters.inbound.http.routers.v1.elevator_router import router as v1_elevator_router

app = FastAPI(
    title="YY Home App",
    description="YY Home App",
    version="1.0.0",
)

load_dotenv()

app.include_router(v1_elevator_router, prefix="/api/v1/elevator", tags=["elevator router v1"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
