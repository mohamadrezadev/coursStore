from fastapi import APIRouter,status,responses,Query,Body,Path ,Depends,Form
from typing import Optional,List,Dict,Any
from sqlalchemy.orm.session import Session
from pydantic import BaseModel
from Data.models import DbUser
from schemas import UserBase,userDisplay
from Data import  db_user
from Data.Database import get_db
import time
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from auth import oauth2

router=APIRouter(prefix="/api/Users",tags=['users'])

async def test_async():
    time.sleep(2)
    return '1'


# @router.post("/signup")
# async def Create_user(user:UserBase, db=Depends(get_db)):
#     return db_user.create_user(db,user)


@router.get("/get_All_users")
async def get_all_users(db=Depends(get_db)):
    return db_user.getAllUsers(db)

@router.get("/get_user")
async def get_user(id:int ,db=Depends(get_db)):
    return db_user.getUser(id,db)

@router.delete("/delete/{id}")
async def delete_user(id:int,db=Depends(get_db)):
    return db_user.deleteUser(id,db)

@router.put("/Update/{id}")
async def update_user(id:int,user:UserBase,db=Depends(get_db)):
    return db_user.updateUser(id,db,user)


@router.get('/me',description="get token and response is data user ")
def  get_me(request:str,db=Depends(get_db)):
    result= oauth2.get_current_user(request,db)
    return result




# @router.post("Create_user/{id}")
# async def Create_user(user:User,id:int,version:int=1):
#     user.id=id
#     return {"response": user,"id":id,"version":version}

# @router.post("Create_user/me/{id}")
# async def me(user:User,
#             id:int=Query(None,title="title text",description="description",alias='UserId',deprecated=False),
#             content:str= Body(...,min_length=10,max_length=30,regex="^[A-Z].*") ,
#             version:int=1):
#     user.id=id
#     return {"response": user,"id":id,"version":version}

# @router.post("getlist_from_user/me/")
# async def getlist(user:User,
#             id_user:int=Query(None,title="title text",description="description",alias='UserId',deprecated=False),
#             content:str= Body(...,min_length=10,max_length=30,regex="^[A-Z].*") ,
#             v: Optional[list[str]]= Query(None),
#             id:int =Path(None,gt=5,le=1),
#             version:int=1):
#     user.id=id
#     return {"response": user,"id":id_user,"id":id,"version":version}
# #Greater than --> Gt
# # Greater or equal to --> GE
# #less than --> Lt
# #less or equal to -->LE

# @router.post("complex_type/")
# async def complex_type(data:data):
#     return {"data":"ok"}