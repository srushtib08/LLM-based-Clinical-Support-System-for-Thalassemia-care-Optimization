from fastapi import APIRouter, HTTPException
from backend.schemas import PatientCreate, PatientUpdate, DonorCreate
from database.db import (
    create_patient_record, get_patient_by_id, update_patient_record,
    delete_patient_record, list_all_patients,
    create_donor_record, find_donors_by_blood_group_and_location
)
from bson import ObjectId

router = APIRouter()

@router.post("/", summary="Create patient")
def create_patient(payload: PatientCreate):
    payload_dict = payload.dict()
    pid = create_patient_record(payload_dict)
    return {"patient_id": pid}

@router.get("/{patient_id}", summary="Get patient")
def get_patient(patient_id: str):
    patient = get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    # convert ObjectId to string
    patient["_id"] = str(patient["_id"])
    return patient

@router.patch("/{patient_id}", summary="Update patient")
def update_patient(patient_id: str, payload: PatientUpdate):
    updated = update_patient_record(patient_id, {k:v for k,v in payload.dict().items() if v is not None})
    if not updated:
        raise HTTPException(status_code=404, detail="Update failed or no changes")
    return {"updated": True}

@router.delete("/{patient_id}", summary="Delete patient")
def delete_patient(patient_id: str):
    deleted = delete_patient_record(patient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Delete failed")
    return {"deleted": True}

@router.get("/", summary="List patients")
def list_patients():
    rows = list_all_patients()
    for r in rows:
        r["_id"] = str(r["_id"])
    return rows

# Donor endpoints (simple)
@router.post("/donors", summary="Create donor")
def add_donor(payload: DonorCreate):
    did = create_donor_record(payload.dict())
    return {"donor_id": did}

@router.get("/donors/search", summary="Find donors")
def search_donors(blood_group: str, location: str):
    donors = find_donors_by_blood_group_and_location(blood_group, location)
    for d in donors:
        d["_id"] = str(d["_id"])
    return donors
