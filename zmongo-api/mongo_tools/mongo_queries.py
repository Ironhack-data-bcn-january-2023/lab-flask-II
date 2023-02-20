from mongo_config.mongo_connection import collection
import pandas as pd


def random_filter ():
    filter = {"founded_year": 2005}
    projection = {"name": 1, 'founded_year': 1,"_id": 0}

    variable = list(collection.find(filter, projection))

    my_dict = {'result': variable}
    return my_dict
     