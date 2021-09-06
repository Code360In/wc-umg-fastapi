from sqlalchemy.orm import Session

import doctor
import paciente
import medicamento
import enfermedad


def get_doctores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(doctor.DoctorList).offset(skip).limit(limit).all()


def get_doctor(db: Session, doctor_id: int):
    return db.query(doctor.DoctorList).filter(doctor.DoctorList.id == doctor_id).first()


def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(paciente.PacienteList).offset(skip).limit(limit).all()


def get_paciente(db: Session, paciente_id: int):
    return db.query(paciente.PacienteList).filter(paciente.PacienteList.id == paciente_id).first()


def get_enfermedades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(enfermedad.EnfermedadList).offset(skip).limit(limit).all()


def get_enfermedad(db: Session, enfermedad_id: int):
    return db.query(enfermedad.EnfermedadList).filter(enfermedad.EnfermedadList.id == enfermedad_id).first()


def get_medicamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(medicamento.MedicamentoList).offset(skip).limit(limit).all()


def get_medicamento(db: Session, medicamento_id: int):
    return db.query(medicamento.MedicamentoList).filter(medicamento.MedicamentoList.id == medicamento_id).first()
