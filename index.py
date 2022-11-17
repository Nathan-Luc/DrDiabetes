# 1. Library imports
from fastapi import FastAPI
import numpy as np
import pandas as pd
from app.formula import predict_diabetes
from config.db import conn
import uvicorn
from route.user import (
    record,
    find_record,
    find_all_records,
    create_records,
    update_record,
    delete_record,
)
from route.doctor import (
    doctor,
    find_doctor,
    find_all_doctors,
    update_doctor,
    create_doctor,
    delete_doctor,
)
from route.patient import (
    patient,
    find_patient,
    find_all_patients,
    create_patient,
    update_patient,
    delete_patient,
)




app = FastAPI()
app.include_router(record)
app.include_router(doctor)
app.include_router(patient)

@app.post('/index/add_doctor')
async def add_doctor(fname:str, lname:str):
    sample_doctor = {
        "fname": fname,
        "lname": lname
    }
    return await create_doctor(sample_doctor)

@app.post('/index/add_patient')
async def add_patient(fname: str, lname: str, DOB: int, gender: bool, family_diabetic: int, d_id: int):
    sample_patient = {
        "fname": fname,
        "lname": lname,
        "DOB": DOB,
        "gender": gender,
        "family_diabetic": family_diabetic,
        "d_id": d_id
    }   
    return await create_patient(sample_patient)

@app.post('/index/add_record')
async def add_record(bp: float, glucose: float, height: float, insulin: float, pedigree: float, pregnancies:int, p_id: int, st: float, weight: float):
    sample_record = {
        "blood_pressure": bp,
        "glucose": glucose,
        "height": height,
        "insulin": insulin,
        "pedigree": pedigree,
        "pregnancies": pregnancies,
        "p_id": p_id,
        "skin_thickness": st,
        "weight": weight
    }
    return await create_records(sample_record)
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

    
#uvicorn indexapp:app --reload