from fastapi import APIRouter
from model.user import User
from config.db import conn
from schema.user import serializeDict,serializeList
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    return serializeList(conn.local.user.find()) 

@user.get('/{id}')
async def find_user(id,user:User):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_users(user:User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find()) 

@user.put('/{id}')
async def update_user(id,user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
         "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user:User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
    