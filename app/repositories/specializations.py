from sqlalchemy import select

from ..models.models import Specialization
from ..db.database import Session



def get_specializations(db: Session):
    specializations = db.scalars(select(Specialization)).all()
    return specializations


def create_specialization(db: Session, specialization: dict):
    specialization = Specialization(name=specialization['name'],
                                    description=specialization['description'])
    db.add(specialization)
    db.commit()
    return specialization


def get_specialization_by_id(db: Session, sid: int):
    specialization = db.get(Specialization, sid)
    print(specialization)
    return specialization