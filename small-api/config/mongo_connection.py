from pymongo import MongoClient
import pandas as pd

client = MongoClient("localhost:27017")
db = client['Ironhack']
employees = db.get_collection('employees')