from pydantic import BaseModel
from typing import List
from fastapi import File
#this class for relationship userDisplayed
class product(BaseModel):
    name:str
    price:int
    description:str
    categories:str
    image:str
    class Config:
        orm_mode=True


class UserBase(BaseModel):
    name:str
    username:str
    email:str
    password:str
    
class AdminUserBase(BaseModel):
    name:str
    username:str
    email:str
    password:str


class userDisplay(BaseModel):
    Name:str
    username: str
    email: str
    products:List[product]

    class Config:
        orm_mode=True


#================================================================


class ProductBase(BaseModel):
    Name:str
    price:int
    description:str
    image:str
    Categories:str
    user_id:int

#this class for relationship productDisplay
class User(BaseModel):
    id:int
    username:str
    class Config:
        orm_mode=True

class productDisplay(BaseModel):
    Name:str
    price:int
    description:str
    image:str
    Categories:str
    user:User

    class Config:
        orm_mode=True
