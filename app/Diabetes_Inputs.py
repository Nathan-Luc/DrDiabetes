from pydantic import BaseModel

class user_input(BaseModel):
    blood_pressure: float
    DOB: int
    gender: bool
    glucose: float
    height: float
    insulin: float
    pedigree: float
    pregancies: int
    skin_thickness: float
    weight: float