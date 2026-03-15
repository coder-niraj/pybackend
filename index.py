from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from database.index import Base,engine
from helpers.index import errorHandler,logger, globalErrorHandler, validationErrorHandler # type: ignore
from routes.index import router
import socketio
import os
from dotenv import load_dotenv
load_dotenv()
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)

app = FastAPI()

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)
@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)
final = socketio.ASGIApp(
    socketio_server=sio,
    other_asgi_app=app
)
@app.get("/")
async def root():
    return {"message": "server running"}
print("server is running on port ",os.getenv("PORT"))
app.middleware("http")(logger) # type: ignore
app.add_exception_handler(RequestValidationError,validationErrorHandler) # type: ignore
app.add_exception_handler(HTTPException,errorHandler) # type: ignore
app.add_exception_handler(Exception,globalErrorHandler) # type: ignore
Base.metadata.create_all(bind=engine)
app.include_router(router)