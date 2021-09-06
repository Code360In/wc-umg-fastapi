from sqlalchemy.orm import Session

import doctor


def get_doctores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(doctor.DoctorList).offset(skip).limit(limit).all()
