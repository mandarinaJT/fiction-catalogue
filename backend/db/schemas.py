import datetime
from typing import List
from pydantic import BaseModel
from enum import Enum

class media_type(Enum):
    MOVIE = 1
    TV = 2
    BOOK = 3
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

class MediaDisplay(BaseModel):
    key: str
    type: media_type
    title: str
    authors: List[str]
    year: int
    poster_url: str