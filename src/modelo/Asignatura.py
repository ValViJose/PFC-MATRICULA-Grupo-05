from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Asignatura(Base):
        __tablename__ = 'asignatura'
        IDAsignatura = Column(Integer, primary_key=True)
        Nombre = Column(String)
        Descripcion = Column(String)
        Creditos = Column(String)
        Ciclo = Column(String)