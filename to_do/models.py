from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from to_do.database import Base
from sqlalchemy.orm import relationship


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)
