from typing import Optional

from pydantic import BaseModel


class Field(BaseModel):
    name: str
    type: Optional[str] = None
    location: Optional[str] = None


class Well(BaseModel):
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
