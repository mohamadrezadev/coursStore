from fastapi import FastAPI,status,Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from enum import Enum
from typing import Optional
from pydantic import  BaseModel
from schemas import AdminUserBase
from router import Service_product,Service_user,blog
from auth import authentication
from Data import models
from Data.Database import engine
from router import file
from exceptions import Emailnotvalid
from fastapi.middleware.cors import CORSMiddleware
from auth.oauth2 import oauth2_scheme,get_current_user
from  fastapi.staticfiles import StaticFiles
import time

app = FastAPI()
origins = [
    "*"
]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Service_user.router)
app.include_router(Service_product.router)
app.include_router(blog.router)
app.include_router(authentication.router)
app.include_router(file.router)

app.mount('/files', StaticFiles(directory='files'), name='files')
models.Base.metadata.create_all(engine)


@app.get('/ping/',tags=['test'], description="this is api for testing")
async def ping():
    return "test ping"

@app.exception_handler(Emailnotvalid)
def email_not_valid(request: Request, exc: Emailnotvalid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)

@app.middleware('http')
async def add_middleware(request: Request, call_next):
    print ('before call')
    Start_time=time.time()
    response=await call_next(request )
    duration=time.time() - Start_time
    print(response.headers)
    response.headers['duration']=str(duration)
    print('after call')
    return response





