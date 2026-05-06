from fastapi import APIRouter, Depends
from requests import Session

from auth.oauth2 import get_current_user
from db import schemas
from db.database import get_db
from db.router_impl import db_diary


router = APIRouter(
    prefix = '/diary',
    tags = ['diary']
)

@router.post('/')
def create_diary_entry(q: schemas.DiaryEntry, db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_diary.create_new_entry(db, q)

@router.get('/')
def get_all_diary_entries(db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_diary.get_all_entries(db)

@router.get('/{id}')
def get_diary_entry_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_diary.get_entry_by_id(db, id)