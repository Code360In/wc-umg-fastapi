from sqlalchemy import Column, Integer, String

from pg_db import Base


## Models
class MedicamentoList(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

