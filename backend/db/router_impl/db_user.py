from sqlalchemy.orm.session import Session
from db.schemas import User
from db.database import get_db
from db.models import DbUser
from fastapi import HTTPException, status

def create_user(db: Session, request: User):
    
    existing_user = db.query(DbUser).filter(DbUser.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this email already exists'
        )
    

    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = request.password #add hashing
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return 'User added'



