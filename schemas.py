from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date

class PatientCreate(BaseModel):
    name: str
    age: int
    blood_group: str
    location: str
    contact: str
    last_transfusion: Optional[date] = None
    chelation_meds: Optional[List[str]] = []

class PatientUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    blood_group: Optional[str]
    location: Optional[str]
    contact: Optional[str]
    last_transfusion: Optional[date]
    chelation_meds: Optional[List[str]]

class DonorCreate(BaseModel):
    name: str
    blood_group: str
    location: str
    contact: str
    available: bool = True
