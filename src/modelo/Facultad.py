from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Facultad(Base):
        __tablename__ = 'facultad'
        IDFacultad = Column(Integer, primary_key=True)
        Nombre = Column(String)
        Nro estudiantes = Column(Integer)
