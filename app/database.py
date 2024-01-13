from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
password = 'Sangita'
host = 'localhost'


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:%s@%s/fastapi'%(password,host)     #'postgresql://<username>:<password>@<ip-address/hostname>/database_name'
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

Sessionlocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

#dependencies
def get_db():
     db = Sessionlocal()
     try:
         yield db
     finally:
         db.close()    