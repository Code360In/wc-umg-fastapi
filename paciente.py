from sqlalchemy import Column, Integer, String

from pg_db import Base


## Models
class PacienteList(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
