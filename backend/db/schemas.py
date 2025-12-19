from pydantic import BaseModel

class User(BaseModel):
    username:str
    email:str
    password:str

class UserDisplay(BaseModel):
    id:int
    username:str
    email:str

class UserAuth(BaseModel):
    id:int
    username:str
    email:str