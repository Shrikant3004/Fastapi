from fastapi import FastAPI,Response,status,HTTPException,Depends

from random import randrange

from psycopg2.extras import RealDictCursor
from typing import List
from . import models
from .routers import user,post,auth



from .database import engine,get_db


models.Base.metadata.create_all(bind = engine)  #creates the table

app = FastAPI()
app.include_router(user.router)  #routing 
app.include_router(post.router)  #routing 
app.include_router(auth.router)  #routing 

@app.get("/")
def root():
    return {"data":"hello world"}




