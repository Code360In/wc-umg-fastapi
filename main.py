from typing import List

from fastapi import Depends, FastAPI
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


@app.get("/pacientes/", response_model=List[schemas.Paciente])
def read_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes


@app.get("/enfermedades/", response_model=List[schemas.Enfermedad])
def read_enfermedades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enfermedades = crud.get_enfermedades(db, skip=skip, limit=limit)
    return enfermedades


@app.get("/medicamentos/", response_model=List[schemas.Medicamento])
def read_medicamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medicamentos = crud.get_medicamentos(db, skip=skip, limit=limit)
    return medicamentos
