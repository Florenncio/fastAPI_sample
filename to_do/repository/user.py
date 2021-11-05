from sqlalchemy.orm import Session
from to_do import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.User, db: Session):
    new_user = models.User(email = request.email, nome = request.nome, password = request.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não foi possivel criar usuario com id {id}')

    return user
