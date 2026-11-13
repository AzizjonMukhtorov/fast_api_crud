from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.specializations import router
from app.api.auth import auth_router
from app.db.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title='CRUD', lifespan=lifespan)

app.include_router(router)
app.include_router(auth_router)
