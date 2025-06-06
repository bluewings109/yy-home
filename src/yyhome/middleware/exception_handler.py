from fastapi import Request
from fastapi.responses import JSONResponse

from yyhome.exceptions.http_status_exception import HTTPStatusException


async def http_status_exception_handler(request: Request, exc: Exception):  # Exception으로 받기
    # exc가 실제로는 HTTPStatusException인지 타입 확인
    if isinstance(exc, HTTPStatusException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    # 다른 예외일 경우 기본 처리
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
