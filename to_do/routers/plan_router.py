from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from to_do import database, schemas
from to_do.repositories import plan_repository

router = APIRouter(prefix="/plans", tags=["Plans"])

get_db = database.get_db


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_plan(request: schemas.Plan.Base, db: Session = Depends(get_db)):
    return plan_repository.create(request, db)


@router.get("/{id_plan}", response_model=schemas.Plan.View)
def get_plan(id_plan: int, db: Session = Depends(get_db)):
    return plan_repository.show(id_plan, db)


@router.put("/{id_plan}", status_code=status.HTTP_202_ACCEPTED)
def update_plan(
    id_plan: int, request: schemas.Plan.Base, db: Session = Depends(get_db)
):
    return plan_repository.update(id_plan, request, db)


@router.delete("/{id_plan}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plan(id_plan: int, db: Session = Depends(get_db)):
    return plan_repository.delete(id_plan, db)
