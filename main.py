from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.specializations import router
from app.db.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title='CRUD', lifespan=lifespan)

app.include_router(router)
