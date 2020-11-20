from typing import Optional, List

from pydantic import BaseModel


class WellCreate(BaseModel):
    name: str
    pad: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    alt: Optional[float] = None
    bottom: Optional[float] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    x: Optional[float] = None
    y: Optional[float] = None


class Well(WellCreate):
    id: int

    class Config:
        orm_mode = True


class FieldCreate(BaseModel):
    name: str
    type: Optional[str] = None
    location: Optional[str] = None
    wells: List[Well] = []


class Field(FieldCreate):
    id: int

    class Config:
        orm_mode = True
