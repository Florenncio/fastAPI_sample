from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from to_do import models, schemas


def create(request: schemas.Task.Create, db: Session):
    new_task = models.Task(
        titulo=request.titulo,
        descricao=request.descricao,
        prioridade=request.prioridade,
        data_inicio=request.data_inicio,
        data_final=request.data_final,
        concluido=request.concluido,
        plan_id=request.plan_id,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def show(id_task: int, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id_task).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Não foi possivel encontrar a tarefa com id {id_task}.",
        )

    return task


def all(db: Session):
    tasks = db.query(models.Task).all()

    return tasks


def update(id_task: int, request: schemas.Task.Base, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id_task)

    if not task.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não foi possivel encontrar a tarefa com id {id_task}.",
        )

    task.update(request.dict())
    db.commit()

    return "atualizado"


def delete(id_task: int, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id_task)

    if not task.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não foi encontrada tarefa com id {id_task}.",
        )

    task.delete(synchronize_session=False)
    db.commit()

    return "deletado"
