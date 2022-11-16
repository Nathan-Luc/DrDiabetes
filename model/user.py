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
    pregancies: int
    skin_thickness: float
    weight: float