from fastapi.routing import APIRouter
from fastapi import Depends

from typing import Annotated

from ..schemas.specializations import (SpecializationCreate, 
                                     SpecializationResponse,
                                     SpecializationUpdate)
from ..db.database import get_db, Session
from ..services.specializations import (create_specialization_service, 
                                        get_specialization_service,
                                        get_specialization_by_id_service)



router = APIRouter(tags=['Specialization'])
DB = Annotated[Session, Depends(get_db)]



@router.get('/specializations', response_model=list[SpecializationResponse])
async def get_specializations(db: DB):
    return get_specialization_service(db)


@router.get('/specialization/{sid}', response_model=SpecializationResponse)
async def get_specialization_by_id(db: DB, sid: int):
    return get_specialization_by_id_service(db, sid)


@router.post('/specialization', response_model=SpecializationResponse, status_code=201)
async def create_specialization(spec: SpecializationCreate, db: DB):
    print(spec)
    return create_specialization_service(db, spec)