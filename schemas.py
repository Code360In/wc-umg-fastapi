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


class PacienteBase(BaseModel):
    id: int
    nombre: str


class Paciente(PacienteBase):
    class Config:
        orm_mode = True


class EnfermedadBase(BaseModel):
    id: int
    nombre: str


class Enfermedad(EnfermedadBase):
    class Config:
        orm_mode = True


class MedicamentoBase(BaseModel):
    id: int
    nombre: str


class Medicamento(MedicamentoBase):
    class Config:
        orm_mode = True
