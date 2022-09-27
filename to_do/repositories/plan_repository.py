from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from to_do import models, schemas


def create(request: schemas.Plan.Create, db: Session):
    new_plan = models.Plan(
        titulo=request.titulo,
        tag=request.tag,
        descricao=request.descricao,
        user_id=request.user_id,
    )

    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return new_plan


def show(id_plan: int, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id_plan).first()
    if not plan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Não foi possivel achar a plano com id {id_plan}.",
        )
    return plan


def update(id_plan: int, request: schemas.Plan.Base, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id_plan)

    if not plan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não possivel encontra a plano com id {id_plan}.",
        )

    plan.update(request.dict())
    db.commit()

    return "atualizado"


def delete(id_plan: int, db: Session):
    plan = db.query(models.Plan).filter(models.Plan.id == id_plan)

    if not plan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não foi possivel encontrar a plano com id {id_plan}.",
        )

    plan.delete(synchronize_session=False)
    db.commit()

    return "deletado"
