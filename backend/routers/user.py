from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm.session import Session
from db import schemas
from db.router_impl import db_user

router = APIRouter(
    prefix = '/users',
    tags = ['users']
)

@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    db_user.create_user(db, request)

