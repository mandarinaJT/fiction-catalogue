from typing import List

from fastapi import APIRouter, Depends
from db import schemas
from auth.oauth2 import get_current_user
from external_api import hardcover

router = APIRouter(
    prefix = '/search',
    tags = ['serach']
)

@router.get('/', response_model = List[schemas.MediaDisplay])
def search(q: str, current_user: schemas.UserAuth = Depends(get_current_user)):
    return hardcover.search(q)