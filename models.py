from pydantic import BaseModel

class Patient(BaseModel):
    id: str
    name: str
    blood_group: str
    last_transfusion: str
    chelation_meds: list

class Donor(BaseModel):
    id: str
    name: str
    location: str
    contact: str
