from .database import Base

from sqlalchemy.sql.expression import text
from sqlalchemy import Column,String,Integer,Boolean,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "sqlalchemy_posts"

    id = Column(Integer,nullable=False,primary_key = True)
    title = Column(String,nullable = False)
    content = Column(String,nullable = False)
    published = Column(Boolean,nullable = False,server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone=True),nullable = False, server_default = text('now()'))
    owner_id = Column(Integer,ForeignKey("Users.id",ondelete="CASCADE"),nullable = False)
    owner = relationship("User")  



class User(Base):
    __tablename__ = "Users"

    id = Column(Integer,nullable=False,primary_key = True)
    email = Column(String,nullable = False,unique=True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable = False, server_default = text('now()'))
