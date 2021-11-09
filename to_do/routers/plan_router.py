from typing import List
from fastapi  import APIRouter, Depends, status, Response
from fastapi.params import Depends
from to_do import database, schemas
from sqlalchemy.orm import Session
from to_do.repositories import plan_repository

router = APIRouter(
    prefix='/plans',
    tags=['Plans']
)

get_db = database.get_db

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_plan(request: schemas.PlanBase, db: Session = Depends(get_db)):
    return plan_repository.create(request, db)

@router.get('/{id}', response_model=schemas.PlanView)
def get_plan(id: int, db: Session = Depends(get_db)):
    return plan_repository.show(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_plan(id:int, request: schemas.PlanBase, db: Session = Depends(get_db)):
    return plan_repository.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_plan(id:int, db: Session = Depends(get_db)):
    return plan_repository.delete(id, db)