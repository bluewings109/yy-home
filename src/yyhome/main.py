import uvicorn
from fastapi import FastAPI

from yyhome.common.router.routers import router

app = FastAPI(
    title="YY Home App",
    description="YY Home App",
    version="1.0.0",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
