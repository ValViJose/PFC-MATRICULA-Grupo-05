from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Profesor(Base):
        __tablename__ = 'profesor'
        IDProfesor = Column(Integer, primary_key=True)
        Nombres = Column(String)
        Apellidos = Column(String)
        Celular = Column(String)
        Email = Column(String)
