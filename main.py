from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import doctor
import schemas
from pg_db import SessionLocal, engine

doctor.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/doctores/", response_model=List[schemas.Doctor])
def read_doctores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctores = crud.get_doctores(db, skip=skip, limit=limit)
    return doctores


@app.get("/doctores/{doctor_id}", response_model=schemas.Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor No encontrado")
    return doctor


@app.get("/pacientes/", response_model=List[schemas.Paciente])
def read_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes


@app.get("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente No encontrado")
    return paciente


@app.get("/enfermedades/", response_model=List[schemas.Enfermedad])
def read_enfermedades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enfermedades = crud.get_enfermedades(db, skip=skip, limit=limit)
    return enfermedades


@app.get("/enfermedades/{emfermedad_id}", response_model=schemas.Enfermedad)
def read_enfermedad(emfermedad_id: int, db: Session = Depends(get_db)):
    enfermedad = crud.get_enfermedad(db, emfermedad_id=emfermedad_id)
    if enfermedad is None:
        raise HTTPException(status_code=404, detail="Enfermedad No encontrada")
    return enfermedad


@app.get("/medicamentos/", response_model=List[schemas.Medicamento])
def read_medicamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medicamentos = crud.get_medicamentos(db, skip=skip, limit=limit)
    return medicamentos


@app.get("/medicamentos/{medicamento_id}", response_model=schemas.Medicamento)
def read_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    medicamento = crud.get_medicamento(db, medicamento_id=medicamento_id)
    if medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento No encontrado")
    return medicamento
