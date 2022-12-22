from Data.Database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

#generate table to database
class DbUser(Base):
    __tablename__ = 'Users'

    id = Column(Integer,index=True,primary_key=True)
    Name=Column(String)
    username=Column(String)
    email=Column(String)
    pwd=Column(String)

    products=relationship('DbProduct',back_populates='user')


class DbProduct(Base):
    __tablename__ = 'Products'

    id=Column(Integer,index=True,primary_key=True)
    Name=Column(String)
    description=Column(String)
    price=Column(Integer)
    image=Column(String)
    Categories=Column(String)

    user_id=Column(Integer,ForeignKey('Users.id'))
    user=relationship('DbUser',back_populates='products')


