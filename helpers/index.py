import time
from typing import Generic, Optional, TypeVar

from fastapi import  HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

async def logger(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start
    print(f"{request.method} {request.url} completed in {process_time:.3f}s")

    return response

async def errorHandler(request:Request,exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success":False,
            "error":{
                "message":exc.detail,
            },
        },
    )
async def globalErrorHandler(request:Request,exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success":False,
            "error":{
                "message":"internal server error",
            },
        },
    )
async def validationErrorHandler(request:Request,exc: RequestValidationError):
    errors=[]
    for err in exc.errors():
        errors.append({
            "field":err["loc"][-1],
            "message":err["msg"],
        })
    return JSONResponse(
        status_code=422,
        content={
            "success":False,
            "error": {
                "message":"Validation Failed",
                "Fields":errors
            }
        }
    )
T = TypeVar("T")
class ApiResponse(BaseModel,Generic[T]):
    success:bool
    data: Optional[T] = None, # type: ignore
class UserResponse(BaseModel):
    id:str
    name:str
    email:str
    class config:
        from_attributes = True