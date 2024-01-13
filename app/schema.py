from pydantic import BaseModel,EmailStr
from datetime import datetime

class POST(BaseModel):
    title:str
    content:str
    published:bool = True


class POST_Create(POST):
    pass

class POST_Update(POST):
    pass 

class User_Response(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime

    class Config:
        orm_mode = True    

class POST_Response(POST):
    created_at:datetime
    owner:User_Response
    class Config:
        orm_mode = True


class User(BaseModel):
    email : EmailStr
    password : str



class Userlogin(BaseModel):
    username:EmailStr
    password:str

class token(BaseModel):
    access_token :str
    token_type :str
    class Config:
        orm_mode = True

class tokendata(BaseModel):
    id:str          

