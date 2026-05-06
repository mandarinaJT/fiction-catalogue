from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from db import schemas
from db.router_impl import db_fiction


router = APIRouter(
    prefix = '/fiction',
    tags = ['fiction']
)

@router.post('/')
def create_fiction(q: schemas.Fiction, db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_fiction.create_fiction(db, q)

@router.get('/', response_model=List[schemas.FictionDisplay])
def get_all_fiction(db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_fiction.get_all_fiction(db)

@router.get('/{id}', response_model=schemas.FictionDisplay)
def get_fiction_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(get_current_user)):
    return db_fiction.get_fiction_by_id(db, id)