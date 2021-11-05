from fastapi import FastAPI
from to_do import  models
from to_do.database import engine
from  to_do.routers import user

app = FastAPI()

models.Base.metadata.create_all()

app.include_router(user.router)