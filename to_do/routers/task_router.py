from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from to_do import database, schemas
from to_do.repositories import task_repository

router = APIRouter(prefix="/tasks", tags=["Tasks"])

get_db = database.get_db


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(request: schemas.Task.Base, db: Session = Depends(get_db)):
    return task_repository.create(request, db)


@router.get("/{id_task}", response_model=schemas.Task.View)
def get_task(id_task: int, db: Session = Depends(get_db)):
    return task_repository.show(id_task, db)


@router.put("/{id_task}", status_code=status.HTTP_202_ACCEPTED)
def update_task(
    id_task: int, request: schemas.Task.Base, db: Session = Depends(get_db)
):
    return task_repository.update(id_task, request, db)


@router.delete("/{id_task}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id_task: int, db: Session = Depends(get_db)):
    return task_repository.delete(id_task, db)
