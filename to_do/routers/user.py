from fastapi  import APIRouter, Depends, status
from fastapi.params import Depends
from to_do import database, schemas
from sqlalchemy.orm import Session
from to_do.repository import user



router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.post('/create')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)