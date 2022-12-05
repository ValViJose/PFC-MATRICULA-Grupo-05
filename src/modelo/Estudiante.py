from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Estudiante(Base):
        __tablename__ = 'estudiante'
        IDEstudiante = Column(Integer, primary_key=True)
        Apellidos = Column(String)
        Nombres = Column(String)
        Sexo = Column(String)
        FechaNacimiento = Column(String)
        Telefono = Column(String)
        Email = Column(String)
