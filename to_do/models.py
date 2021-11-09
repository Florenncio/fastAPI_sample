from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from to_do.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)
    
    plans = relationship('Plan', back_populates='users')

class Plan(Base):

    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    tag = Column(String)
    
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('User', back_populates='plans')
    
    tasks = relationship('Task', back_populates='plans')

class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    prioridade = Column(Integer)
    data_inicio = Column(DateTime)
    data_final = Column(DateTime)
    concluido = Column(Boolean, default=False)

    plans = relationship('Plan', back_populates='tasks')
    plans_id = Column(Integer, ForeignKey('plans.id'))