from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


DATABASE = 'sqlite:///./med.db'

engine = create_engine(
    DATABASE,
    connect_args={'check_same_thread': False},
    echo=True
)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

def get_db():
    with SessionLocal() as sesssion:
        yield sesssion
