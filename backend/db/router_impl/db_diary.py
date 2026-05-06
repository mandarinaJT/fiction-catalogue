from fastapi import HTTPException, status
from requests import Session

from db.models import DbDiaryEntry, DbFiction
from db.schemas import DiaryEntry


def create_new_entry(db: Session, request: DiaryEntry):

    fiction = db.query(DbFiction).filter(DbFiction.id == request.fiction_id).first()
    if not fiction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Fiction not found')
    new_entry = DbDiaryEntry(
        fiction_id = request.fiction_id,
        score = request.score,
        date = request.date,
        comment = request.comment
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return 'Entry added'

def get_all_entries(db: Session):

    entries = db.query(DbDiaryEntry.id,
                 DbDiaryEntry.score,
                 DbDiaryEntry.date,
                 DbDiaryEntry.comment,
                 DbDiaryEntry.fiction_id,
                 DbFiction.name,
                 DbFiction.author,
                 DbFiction.medium
                ).join(DbFiction, DbDiaryEntry.fiction_id == DbFiction.id
                ).all()
    
    return [
        {
            "id": entry[0],
            "score": entry[1],
            "date": entry[2],
            "comment": entry[3],
            "fiction_id": entry[4],
            "fiction_name": entry[5],
            "fiction_author": entry[6],
            "fiction_medium": entry[7]
        }
        for entry in entries
    ]


def get_entry_by_id(db: Session, entry_id: int):

    entry = db.query(DbDiaryEntry.id,
                 DbDiaryEntry.score,
                 DbDiaryEntry.date,
                 DbDiaryEntry.comment,
                 DbDiaryEntry.fiction_id,
                 DbFiction.name,
                 DbFiction.author,
                 DbFiction.medium).join(DbFiction, DbDiaryEntry.fiction_id == DbFiction.id).filter(DbDiaryEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Diary entry not found')
    return {
        "id": entry[0],
        "score": entry[1],
        "date": entry[2],
        "comment": entry[3],
        "fiction_id": entry[4],
        "fiction_name": entry[5],
        "fiction_author": entry[6],
        "fiction_medium": entry[7]
    }