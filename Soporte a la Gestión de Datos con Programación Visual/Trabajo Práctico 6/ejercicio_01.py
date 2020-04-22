# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String, UniqueConstraint,MetaData
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer,primary_key=True,unique=True)
    dni = Column(Integer,unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))

"""
engine = create_engine('sqlite:///socios.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

Base.metadata.create_all(engine)"""




