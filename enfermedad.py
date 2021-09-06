from sqlalchemy import Column, Integer, String

from pg_db import Base


## Models
class EnfermedadList(Base):
    __tablename__ = "enfermedades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

