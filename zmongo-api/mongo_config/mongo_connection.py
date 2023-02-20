from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client["Ironhack"]
collection = db.get_collection("companies")