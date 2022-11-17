from fastapi import APIRouter
from model.user import Patient
from config.db import conn
from schema.user import serializeDict,serializeList
from bson import ObjectId

patient = APIRouter()
# CRUD

async def find_all_patients():
    return serializeList(conn.local.patient.find()) 

async def find_patient(id):
    return serializeDict(conn.local.patient.find_one({"_id":ObjectId(id)}))

async def create_patient(patient:Patient):
    conn.local.patient.insert_one(dict(patient))
    return serializeList(conn.local.patient.find()) 

async def update_patient(id,patient:Patient):
    conn.local.patient.find_one_and_update({"_id":ObjectId(id)},{
         "$set":dict(patient)
    })
    return serializeDict(conn.local.patient.find_one({"_id":ObjectId(id)}))

async def delete_patient(id,patient:Patient):
    return serializeDict(conn.local.patient.find_one_and_delete({"_id":ObjectId(id)}))
