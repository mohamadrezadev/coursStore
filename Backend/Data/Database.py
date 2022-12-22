from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship

engine= create_engine("sqlite:///FastApi.db", connect_args={'check_same_thread':False} )
Base=declarative_base()

#for connection to database
session_local=sessionmaker(bind=engine,autocommit=False,autoflush=False)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
