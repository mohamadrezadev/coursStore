from fastapi import APIRouter,Depends,status,Response
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from pydantic import BaseModel
from Data.Database import get_db
from Data import db_user
from schemas import UserBase,userDisplay
from Data.hash import Hash
from auth import oauth2
from Data import models
from Data.db_user import getUserByUsername
router=APIRouter(tags=['authentication'])

@router.post('/signin')
def get_token(request:OAuth2PasswordRequestForm=Depends(),
                db:Session=Depends(get_db)):

    # user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    user=getUserByUsername(request.username,db)
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credential')

    if not Hash.verify(user.pwd, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')

    access_token = oauth2.create_access_token(data={'sub':request.username})
    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username
    }
class Response(BaseModel):
    UserData:userDisplay
    Token:str

@router.post("/signup" )
async def Create_user(user:UserBase, db=Depends(get_db)):
    result= db_user.create_user(db,user)
    if result!=False:
        print("User created successfully")
        access_token = oauth2.create_access_token(data={'sub':user.username})
        return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': result.id,
        'username': result.username
    }
    print("user already exists")
    return "user already exists"

