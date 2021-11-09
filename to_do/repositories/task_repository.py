from sqlalchemy.orm import Session
from to_do import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.TaskCreate, db: Session):
    new_task = models.Task(
        titulo = request.titulo, 
        descricao = request.descricao, 
        prioridade = request.prioridade,
        data_inicio = request.data_inicio,
        data_final = request.data_final,
        concluido = request.concluido,
        plans_id = request.plan_id,
        )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def show(id: int, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel encontrar a tarefa com id {id}.'
            )
    
    return task

def update(id: int, request: schemas.TaskBase, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id)
    
    if not task.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Não foi possivel encontrar a tarefa com id {id}.'
            )
    
    task.update(request.dict())
    db.commit()

    return 'atualizado'

def delete(id: int, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id)

    if not task.first():
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail= f'Não foi encontrada tarefa com id {id}.'
            )

    task.delete(synchronize_session=False)
    db.commit()

    return 'deletado'