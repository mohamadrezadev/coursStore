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

class Item(BaseModel):
    email: str = ""
    name: str = ""
    password: str = ""
    username: str = ""

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/Users/Create_user")
async def create_user(user:Item):
    print(user)
    # return db_user.create_user(db,user)


