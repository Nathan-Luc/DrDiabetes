from pydantic import BaseModel

class Record(BaseModel):
    blood_pressure: float
    glucose: float
    height: float
    insulin: float
    pedigree: float
    pregnancies: int
    patient_id: int
    skin_thickness: float
    weight: float

class Patient(BaseModel):
    f_name: str
    l_name: str
    DOB: int
    gender: bool
    family_diabtic: int
    d_id: int

class Doctor(BaseModel):
    f_name: str
    l_name: str
    