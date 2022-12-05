from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Notas(Base):
        __tablename__ = 'notas'
        IDEstudiante = Column(
            Integer,
            ForeignKey('estudiante.IDEstudiante'),
            primary_key=True)
        IDAsignatura = Column(
            Integer,
            ForeignKey('Asignatura.IDAsignatura'),
            primary_key=True)

        C1 = Column(Integer)
        EP = Column(Integer)
        C2 = Column(Integer)
        EF = Column(Integer)