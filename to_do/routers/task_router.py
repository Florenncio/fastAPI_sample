from typing import List
from fastapi  import APIRouter, Depends, status, Response
from fastapi.params import Depends
from to_do import database, schemas
from sqlalchemy.orm import Session
from to_do.repositories import task_repository

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

get_db = database.get_db


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_task(request: schemas.TaskBase, db: Session = Depends(get_db)):
    return task_repository.create(request, db)

@router.get('/{id}', response_model=schemas.TaskView)
def get_task(id: int, db: Session = Depends(get_db)):
    return task_repository.show(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_task(id: int, request: schemas.TaskBase, db: Session = Depends(get_db)):
    return task_repository.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db: Session = Depends(get_db)):
    return task_repository.delete(id, db)