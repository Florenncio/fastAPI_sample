from enum import IntEnum, Enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


#Choises
class PlanEnum(str, Enum):
    pessoal = 'pessoal'
    profissional = 'profissional'
    estudos = 'estudo'
    off_topic = 'off-topic'

class TaskEnum(IntEnum):
    baixa = 4
    media = 3
    alta = 2
    urgente = 1


#Tasks
class TaskBase(BaseModel):
    titulo:str
    descricao:str
    prioridade:TaskEnum
    data_inicio:datetime
    data_final:datetime
    concluido:bool
    plans_id:int

class TaskCreate(TaskBase):
    pass

class TaskView(TaskBase):
    titulo:str
    descricao:str
    prioridade:TaskEnum
    data_inicio:datetime
    data_final:datetime
    concluido:bool
    plans_id:int
    
    class Config():
        orm_mode = True

class TaskViewPlan(TaskBase):
    titulo:str
    descricao:str
    prioridade:TaskEnum
    data_inicio:datetime
    data_final:datetime
    concluido:bool
    plans_id:int
    
    class Config():
        orm_mode = True


#Plans
class PlanBase(BaseModel):
    titulo:str
    tag:PlanEnum
    users_id:int

class PlanCreate(PlanBase):
    pass

class PlanView(PlanBase):  
    titulo:str
    tag:PlanEnum
    users_id:int
    
    class Config():
        orm_mode = True

class PlanViewUser(PlanBase):  
    titulo:str
    tag:PlanEnum  
    
    class Config():
        orm_mode = True


#Users
class UserBase(BaseModel):
    nome:str
    email:str
    password:str

class UserCreate(UserBase):
    pass


class UserView(BaseModel):
    nome:str
    email:str
    plans:List[PlanViewUser] = []

    class Config():
        orm_mode = True