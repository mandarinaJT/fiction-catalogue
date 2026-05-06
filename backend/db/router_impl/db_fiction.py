from fastapi import HTTPException, status
from requests import Session

from db.models import DbFiction
from db.schemas import Fiction, FictionDisplay


def create_fiction(db: Session, request: Fiction):

    new_fiction = DbFiction(
        name = request.name,
        author = request.author,
        medium = request.medium
    )

    db.add(new_fiction)
    db.commit()
    db.refresh(new_fiction)

    return 'Fiction added'

def get_all_fiction(db: Session):

    fiction = db.query(DbFiction.id,
                 DbFiction.name,
                 DbFiction.author,
                 DbFiction.medium
                ).all()
    
    return [
        {
            "id": fict[0],
            "name": fict[1],
            "author": fict[2],
            "medium": fict[3].value
        }
        for fict in fiction
    ]

def get_fiction_by_id(db: Session, fiction_id: int):

    fiction = db.query(DbFiction).filter(DbFiction.id == fiction_id).first()
    if not fiction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Fiction not found')
    return FictionDisplay(
        id = fiction.id,
        name = fiction.name,
        author = fiction.author,
        medium = fiction.medium.value
    )

