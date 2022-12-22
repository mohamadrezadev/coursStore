from sqlalchemy.orm.session import Session
from schemas import UserBase
from Data.models import DbUser
from Data.hash import Hash
from exceptions import Emailnotvalid

#create user
def create_user(db:Session , request:UserBase):
    if "@" not in request.email:
        raise Emailnotvalid('Email not valid')
    user =getUserByUsername(request.username ,db)
    if  user is None:
        newuser=DbUser(
            Name=request.name,
            username=request.username,
            email=request.email,
            pwd=Hash.bcrypt(request.password)
        )
        db.add(newuser)
        db.commit()
        db.refresh(newuser)
        return newuser
    print('user already exists')
    return False


def find_user(db:Session,username1:str):
    user_founded=db.query(DbUser).filter(DbUser.username==username1).first()
    if user_founded is not None:
        return False
    return True
#get All Users
def getAllUsers(db:Session):
    return db.query(DbUser).all()
#get user by username
def getUserByUsername(username:str,db:Session):

    return db.query(DbUser).filter(DbUser.username==username).first()

#get User
def getUser(id:int,db:Session):
    return db.query(DbUser).filter(DbUser.id == id).first()

#delete User
def deleteUser(id:int, db:Session):
    User=getUser(id,db)
    db.delete(User)
    db.commit()
    return 'deleted successfully'

# update User
def updateUser(id:int,db:Session,request:UserBase):
    user=db.query(DbUser).filter(DbUser.id ==id)
    user.update({
        DbUser.Name: request.Name,
        DbUser.username: request.Username,
        DbUser.email: request.email,
        DbUser.pwd: Hash.bcrypt(request.Password),
    })
    db.commit()
    return 'updated successfully'
