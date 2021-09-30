from fastapi import FastAPI
from bson import ObjectId
from schemas.schema import *
from models.model import *
from config.db import db
app = FastAPI()

@app.get('/user')
async def list_users():
    user_documnets = db.users.find()
    return usersEntity(user_documnets)

@app.get('/user/{id}')
async def find_one_user(id):
    user_document = db.users.find_one({"_id":ObjectId(id)})
    return userEntity(user_document)

@app.post('/user')
async def create_user(user: User):
    db.users.insert_one(dict(user))
    return {"message": "inserted"}

@app.put('/user/{id}')
async def update_user(id,user: User):
    db.users.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return {"message": "updated"}

@app.delete('/user/{id}')
async def delete_user(id,user: User):
    deleted_document = userEntity(db.users.find_one_and_delete({"_id":ObjectId(id)}))
    return {"message": "deleted", "data": deleted_document}

@app.get("/")
async def root():
    return {"message": "hi! please use docs for end points"}
