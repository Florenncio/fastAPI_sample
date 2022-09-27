from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from to_do.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)

    plans = relationship("Plan")


class Plan(Base):

    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    tag = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="plans")
    tasks = relationship("Task")


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    prioridade = Column(Integer)
    data_inicio = Column(DateTime)
    data_final = Column(DateTime)
    concluido = Column(Boolean, default=False)
    plan_id = Column(Integer, ForeignKey("plans.id"))

    plans = relationship("Plan", back_populates="tasks")
