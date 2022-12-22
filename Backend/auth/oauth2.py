from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from Data.Database import get_db
from Data.db_user import getUserByUsername
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY='6c7d438d2ea66cc11ee315566bda6f45336930dc2a40eaa96ec009524c20aa69'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTE=60

def create_access_token(data:dict,expires_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expires_delta :
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(token: str=Depends(oauth2_scheme), db: Session= Depends(get_db)):
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='invalid credentials',
                                    headers={'WWW-authenticate': 'bearer'})
    try:
        _dict=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username=_dict.get('sub')
        if not username:
            raise error_credential
    except:
        raise error_credential
    user =getUserByUsername(username,db)
    return user
