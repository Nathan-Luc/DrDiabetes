from pydantic import BaseModel

class User(BaseModel):
    blood_pressure: float
    DOB: int
    gender: bool
    glucose: float
    height: float
    insulin: float
    name: str
    pedigree: float
    pregnancies: int
    skin_thickness: float
    weight: float

class Patient(BaseModel):
    f_name: str
    l_name: str
    id: int

class Doctor(BaseModel):
    f_name: str
    l_name: str
    id: int