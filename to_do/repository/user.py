from sqlalchemy.orm import Session
from to_do import models, schemas
from fastapi import HTTPException, status

def create():
    new_user = models.User()
