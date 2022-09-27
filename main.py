from fastapi import FastAPI

from to_do import models
from to_do.database import engine
from to_do.routers import plan_router, task_router, user_router

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user_router.router)
app.include_router(plan_router.router)
app.include_router(task_router.router)
