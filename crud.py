from sqlalchemy.orm import Session

import doctor
import paciente
import medicamento
import enfermedad


def get_doctores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(doctor.DoctorList).offset(skip).limit(limit).all()


def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(paciente.PacienteList).offset(skip).limit(limit).all()


def get_enfermedades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(enfermedad.EnfermedadList).offset(skip).limit(limit).all()


def get_medicamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(medicamento.MedicamentoList).offset(skip).limit(limit).all()
