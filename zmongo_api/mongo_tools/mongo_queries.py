from mongo_config.mongo_connection import collection
import pandas as pd


def random_filter ():
    filter = {"founded_year": 2005}

    variable = list(collection.find(filter))

    my_dict = {'result': variable}
    return my_dict
     