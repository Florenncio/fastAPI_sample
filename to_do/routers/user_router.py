from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from to_do import database, schemas
from to_do.repositories import user_repository

router = APIRouter(prefix="/user", tags=["Users"])

get_db = database.get_db


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User.Create, db: Session = Depends(get_db)):
    return user_repository.create(request, db)


@router.get("/{id_user}", response_model=schemas.User.View)
def get_user(id_user: int, db: Session = Depends(get_db)):
    return user_repository.show(id_user, db)


@router.get("get/all", response_model=List[schemas.User.View])
def get_all_users(db: Session = Depends(get_db)):
    return user_repository.all(db)
