from pydantic import BaseModel
from typing import List

class DoctorBase(BaseModel):
    id: int
    nombre: str
    direccion: str
    telefono: str

class Doctor(DoctorBase):
    class Config:
        orm_mode = True