from fastapi import APIRouter
from model.user import Doctor
from config.db import conn
from schema.user import serializeDict,serializeList
from bson import ObjectId

doctor = APIRouter()
# CRUD

async def find_all_doctors():
    return serializeList(conn.local.doctor.find()) 

async def find_doctor(id):
    return serializeDict(conn.local.doctor.find_one({"_id":ObjectId(id)}))

async def create_doctor(doctor:Doctor):
    conn.local.doctor.insert_one(dict(doctor))
    return serializeList(conn.local.doctor.find()) 

async def update_doctor(id,doctor:Doctor):
    conn.local.doctor.find_one_and_update({"_id":ObjectId(id)},{
         "$set":dict(doctor)
    })
    return serializeDict(conn.local.doctor.find_one({"_id":ObjectId(id)}))

async def delete_doctor(id,doctor:Doctor):
    return serializeDict(conn.local.doctor.find_one_and_delete({"_id":ObjectId(id)}))
