from pymongo import MongoClient
from datetime import datetime
import os

# Load environment variables for DB URI
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = "thalcare_ai"

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Define patient collection
patients_collection = db["patients"]

# ---------------------- Patient DB Functions ---------------------- #

def create_patient_record(patient_data: dict) -> str:
    """
    Inserts a new patient record into the database.
    """
    result = patients_collection.insert_one(patient_data)
    return str(result.inserted_id)


def get_patient_by_id(patient_id: str) -> dict:
    """
    Fetches a patient's record using their MongoDB ID.
    """
    from bson.objectid import ObjectId
    return patients_collection.find_one({"_id": ObjectId(patient_id)})


def update_patient_record(patient_id: str, update_fields: dict) -> bool:
    """
    Updates specified fields in a patient's record.
    """
    from bson.objectid import ObjectId
    result = patients_collection.update_one(
        {"_id": ObjectId(patient_id)},
        {"$set": update_fields}
    )
    return result.modified_count > 0


def delete_patient_record(patient_id: str) -> bool:
    """
    Deletes a patient record by ID.
    """
    from bson.objectid import ObjectId
    result = patients_collection.delete_one({"_id": ObjectId(patient_id)})
    return result.deleted_count > 0


def list_all_patients() -> list:
    """
    Returns a list of all patient records.
    """
    return list(patients_collection.find())


# ---------------------- Example Usage ---------------------- #

if __name__ == "__main__":
    # Example patient data
    new_patient = {
        "name": "Sita Kumari",
        "blood_group": "B+",
        "age": 14,
        "last_transfusion": str(datetime.now().date()),
        "chelation_meds": ["Desferal", "Deferasirox"],
        "location": "Patna, Bihar",
        "contact": "+91XXXXXXXXXX"
    }

    # Create
    patient_id = create_patient_record(new_patient)
    print("Patient created with ID:", patient_id)

    # Read
    patient = get_patient_by_id(patient_id)
    print("Fetched Patient:", patient)

    # Update
    update_patient_record(patient_id, {"age": 15})

    # List
    print("All Patients:", list_all_patients())
