from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from to_do import models, schemas
from to_do.hashing import Hash


def create(request: schemas.User.Create, db: Session):
    new_user = models.User(
        email=request.email,
        nome=request.nome,
        password=Hash.bcrypt(request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def show(id_user: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id_user).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não foi possivel criar usuario com id {id_user}.",
        )

    return user


def all(db: Session):
    users = db.query(models.User).all()

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não foi possicel encontrar o usuarios.",
        )

    return users
