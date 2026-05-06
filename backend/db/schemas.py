from typing import List
from pydantic import BaseModel
from enum import Enum
from datetime import date

class media_type(Enum):
    MOVIE = "movie"
    TV_SHOW = "tv_show"
    BOOK = "book"
    ANIME = "anime"
    MANGA = "manga"
    ANIMANGA = "animanga"
    VIDEO_GAME = "video_game"


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

class Fiction(BaseModel):
    name: str
    author: str
    medium: media_type

class FictionDisplay(Fiction):
    id: int

class DiaryEntry(BaseModel):
    fiction_id: int
    score: int
    date: date
    comment: str

