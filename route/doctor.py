from fastapi import APIRouter
from model.user import Doctor
from config.db import conn
from schema.user import serializeDict,serializeList
from route.user import user_route
from bson import ObjectId

doctor = APIRouter()

u_route = user_route()
# CRUD

@staticmethod
@doctor.get('/doctor')
async def find_all_users():
    return serializeList(conn.local.doctor.find()) 

@doctor.get('/doctor/{id}')
async def find_user(id):
    return serializeDict(conn.local.doctor.find_one({"_id":ObjectId(id)}))

@doctor.get('/doctor-{name}')
async def find_username(name):
    return serializeDict(conn.local.doctor.find_one({"name": name}))

@doctor.post('/doctor/')
async def create_users(doctor:Doctor):
    conn.local.doctor.insert_one(dict(doctor))
    return serializeList(conn.local.doctor.find()) 

@doctor.put('/doctor/{id}')
async def update_user(id,doctor:Doctor):
    conn.local.doctor.find_one_and_update({"_id":ObjectId(id)},{
         "$set":dict(doctor)
    })
    return serializeDict(conn.local.doctor.find_one({"_id":ObjectId(id)}))

@doctor.delete('/doctor/{id}')
async def delete_user(id,doctor:Doctor):
    return serializeDict(conn.local.doctor.find_one_and_delete({"_id":ObjectId(id)}))

@doctor.post('/doctor/patient')
async def get_patient_id():
    patient = await u_route.find_all_users()
    patient_name = await u_route.find_username('Colleen')
    return patient, patient_name