from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

def create_models(tablename):

    class Matricula(Base):
        __tablename__ = 'matricula'
        IDMatricula = Column(Integer, primary_key=True)
        IDEstudiante = Column(
            Integer,
            ForeignKey('estudiante.IDEstudiante'),
            primary_key=True)
        IDAsignatura = Column(
            Integer,
            ForeignKey('asignatura.IDAsignatura'),
            primary_key=True)
        IDProfesor = Column(
            Integer,
            ForeignKey('profesor.IDProfesor'),
            primary_key=True)
        Fecha = Column(Date)
        Hora = Column(String)
        Beca = Column(string)