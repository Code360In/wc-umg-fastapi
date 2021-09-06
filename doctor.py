from sqlalchemy import Column, Integer, String

from pg_db import Base


## Models
class DoctorList(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    telefono = Column(String)
