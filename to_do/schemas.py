from datetime import datetime
from enum import Enum, IntEnum
from typing import List

from pydantic import BaseModel, EmailStr


class Choice:
    class PlanEnum(str, Enum):
        pessoal = "pessoal"
        profissional = "profissional"
        estudos = "estudo"
        off_topic = "off-topic"

    class TaskEnum(IntEnum):
        baixa = 4
        media = 3
        alta = 2
        urgente = 1


class Task:
    class Base(BaseModel):
        titulo: str
        descricao: str
        prioridade: Choice.TaskEnum
        data_inicio: datetime
        data_final: datetime
        concluido: bool = False
        plan_id: int

        class Config:
            orm_mode = True

    class Create(Base):
        pass

    class View(Base):
        titulo: str
        descricao: str
        prioridade: Choice.TaskEnum
        data_inicio: datetime
        data_final: datetime
        concluido: bool
        plan_id: int

        class Config:
            orm_mode = True


class Plan:
    class Base(BaseModel):
        titulo: str
        descricao: str
        tag: Choice.PlanEnum
        user_id: int

        class Config:
            orm_mode = True

    class Create(Base):
        pass

    class View(Base):
        titulo: str
        descricao: str
        tag: Choice.PlanEnum
        user_id: int
        tasks: List[Task.Base]

        class Config:
            orm_mode = True


class User:
    class Base(BaseModel):
        nome: str
        email: EmailStr
        password: str

    class Create(Base):
        pass

    class View(BaseModel):
        nome: str
        email: str
        plans: List[Plan.Base]

        class Config:
            orm_mode = True
