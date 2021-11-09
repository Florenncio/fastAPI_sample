from fastapi  import APIRouter, Depends, status, Response
from fastapi.params import Depends
from to_do import database, schemas
from sqlalchemy.orm import Session
from to_do.repositories import user_repository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_repository.create(request, db)

@router.get('/{id}', response_model=schemas.UserView)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_repository.show(id, db)