from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import doctor_crud
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
    users = doctor_crud.get_doctores(db, skip=skip, limit=limit)
    return users
