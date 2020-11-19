from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    location = Column(String)

    wells = relationship("Well", back_populates="field")


class Well(Base):
    __tablename__ = "wells"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    pad = Column(String)
    type = Column(String)
    status = Column(String)
    alt = Column(Numeric)
    bottom = Column(Numeric)
    lat = Column(Numeric)
    lng = Column(Numeric)
    x = Column(Numeric)
    y = Column(Numeric)

    field = relationship("Field", back_populates="wells")
