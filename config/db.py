from pymongo import MongoClient
conn = MongoClient()
db = conn["todo_db"]