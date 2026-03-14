from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from database.index import Base,engine
from helpers.index import errorHandler,logger, globalErrorHandler, validationErrorHandler # type: ignore
from routes.index import router

import os
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()

app.add_middleware(CORSMiddleware,
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_origins=["*"]
)
print("server is running on port ",os.getenv("PORT"))
app.middleware("http")(logger) # type: ignore
app.add_exception_handler(RequestValidationError,validationErrorHandler) # type: ignore
app.add_exception_handler(HTTPException,errorHandler) # type: ignore
app.add_exception_handler(Exception,globalErrorHandler) # type: ignore
Base.metadata.create_all(bind=engine)
app.include_router(router)