# 1. Library imports
from  app.Diabetes_Inputs import user_input
from fastapi import FastAPI, Form
import numpy as np
import pickle
import pandas as pd
from route.user import user
import uvicorn
from datetime import date

app = FastAPI()
app.include_router(user)
pickle_in = open("model/model.pkl","rb")
model = pickle.load(pickle_in)

def calulate_age(DOB):
    today = date.today()
    return today.year - int(str(DOB)[-4:])
def calculate_bmi(height,weight):
    return ((703*weight) / (height*height))

#@app.get('/')
#def index():
#    return {'message': 'Hello, World'}

@app.get('/user_input')
async def user_details(blood_pressure: int = Form()):
    return {"blood_pressure": blood_pressure}

#@app.get('/user_input/family')
#def 

@app.post('/predict')
def predict_diabetes(data:user_input):
    data = data.dict()
    blood_pressure = data['blood_pressure']
    age = calulate_age(data['DOB'])
    gender = data['gender']
    glucose = data['glucose']
    bmi = calculate_bmi(data['height'],data['weight'])
    insulin = data['insulin']
    pregancies = data['pregancies']
    skin_thickness = data['skin_thickness']
    predigree = data['pedigree']

    prediction = model.predict([[pregancies,glucose,blood_pressure,skin_thickness,insulin,bmi,predigree,age]])

    if prediction[0] == 1:
        preditcion = 'Most Likely have Diabetes'
    else:
        preditcion = 'Most Likely NOT to have Diabetes'
    return{
        'prediction': preditcion
    }
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

    
#uvicorn app/app:app --reload