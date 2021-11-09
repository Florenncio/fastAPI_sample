from sqlalchemy.orm import Session
from to_do import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.PlanCreate, db: Session):
    new_plan = models.Plan(
        titulo = request.titulo,
        tag = request.tag,
        users_id = request.users_id,
    )

    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return new_plan

def show(id: int, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id)

    if not plan:
        raise HTTPException(
            statuts_code = status.HTTP_400_BAD_REQUEST,
            detail= f'Não foi possivel achar a plano com id {id}.'
            )
    return plan

def update(id: int, request: schemas.PlanBase, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id)

    if not plan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não possivel encontra a plano com id {id}.'
            )
    
    plan.update(request.dict())
    db.commit()

    return 'atualizado'

def delete(id: int, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id)

    if not plan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não foi possivel encontrar a plano com id {id}.'
        )
    
    plan.delete(synchronize_session=False)
    db.commit()

    return 'deletado'