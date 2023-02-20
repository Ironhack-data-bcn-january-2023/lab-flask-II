from config import mongo_connection as mongo
from pymongo import MongoClient


def get_basic_info():
    filter = {}
    projection = {'EmployeeNumber':1,'Age':1,'Department':1}
    return mongo.employees.find(filter,projection)

'''def get_everything_table ():
    query = f"SELECT * FROM  salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (table_q):
    query = f"SELECT * FROM  {table_q} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")'''