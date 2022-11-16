from fastapi import APIRouter
from model.user import User
from config.db import conn
from schema.user import serializeDict,serializeList
from bson import ObjectId
import pickle
from datetime import date

user = APIRouter()

# Model Load
pickle_in = open("model/model.pkl","rb")
model = pickle.load(pickle_in)

class user_route():
    # Formula functions
    def calulate_age(DOB):
        today = date.today()
        return today.year - int(str(DOB)[-4:])

    def calculate_bmi(height,weight):
        return ((703*weight) / (height*height))

    # CRUD
    @staticmethod
    @user.get('/user')
    async def find_all_users():
        return serializeList(conn.local.user.find()) 

    @staticmethod
    @user.get('/user/{id}')
    async def find_user(id):
        return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

    @staticmethod
    @user.get('/user-{name}')
    async def find_username(name):
        return serializeDict(conn.local.user.find_one({"name": name}))

    @staticmethod
    @user.post('/user/')
    async def create_users(user:User):
        conn.local.user.insert_one(dict(user))
        return serializeList(conn.local.user.find()) 
    
    @staticmethod
    @user.put('/user/{id}')
    async def update_user(id,user:User):
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
            "$set":dict(user)
        })
        return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))
    
    @staticmethod
    @user.delete('/user/{id}')
    async def delete_user(id,user:User):
        return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))


    # Prediction Model 
    @user.post('/user/predict-{id}')
    async def predict_diabetes(id):
        patient = await find_user(id)
        
        blood_pressure = patient['blood_pressure']
        age = calulate_age(patient['DOB'])
        gender = patient['gender']
        glucose = patient['glucose']
        bmi = calculate_bmi(patient['height'],patient['weight'])
        insulin = patient['insulin']
        pregnancies = patient['pregnancies']
        skin_thickness = patient['skin_thickness']
        predigree = patient['pedigree']

        prediction = model.predict([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,predigree,age]])
        
        if prediction[0] == 1:
            preditcion = 'Most Likely have Diabetes'
        else:
            preditcion = 'Most Likely NOT to have Diabetes'
        return{
            'prediction': preditcion
        }