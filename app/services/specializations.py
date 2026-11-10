from ..repositories.specializations import get_specializations, create_specialization, get_specialization_by_id
from ..schemas.specializations import SpecializationCreate



def create_specialization_service(db, specialization: SpecializationCreate):
    data = specialization.model_dump()
    print(data)
    response = create_specialization(db, data)
    return response

def get_specialization_service(db):
    response = get_specializations(db)
    print(response)
    return response


def get_specialization_by_id_service(db, sid):
    response = get_specialization_by_id(db, sid)
    return response