from fastapi import APIRouter
from model.user import Record
from config.db import conn
from schema.user import serializeDict,serializeList
from bson import ObjectId


record = APIRouter()

# CRUD
async def find_all_records():
    return serializeList(conn.local.record.find()) 

async def find_record(id):
    return serializeDict(conn.local.record.find_one({"_id":ObjectId(id)}))

async def create_records(record:Record):
    conn.local.record.insert_one(dict(record))
    return serializeList(conn.local.record.find()) 

async def update_record(id,record:Record):
    conn.local.record.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(record)
    })
    return serializeDict(conn.local.record.find_one({"_id":ObjectId(id)}))

async def delete_record(id,record:Record):
    return serializeDict(conn.local.record.find_one_and_delete({"_id":ObjectId(id)}))

