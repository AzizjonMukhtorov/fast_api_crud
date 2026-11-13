from sqlalchemy import String, Text, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base



class Specialization(Base):
    __tablename__ = 'specializations'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str|None] = mapped_column(Text, nullable=True)
    
    doctors: Mapped[list['Doctor']] = relationship(back_populates='specialization')


class Doctor(Base):
    __tablename__ = 'doctors'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(String(200), nullable=False)
    specialization_id: Mapped[int] = mapped_column(ForeignKey('specializations.id'))
    experience_years: Mapped[int] = mapped_column(CheckConstraint('experience_years > 0', name='check_experience_years'), nullable=False)
    consultation_price: Mapped[int] = mapped_column(CheckConstraint('consultation_price > 0', name='check_consultation_price'), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    specialization: Mapped['Specialization'] = relationship(back_populates='doctors')
    
    
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default='user')
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
