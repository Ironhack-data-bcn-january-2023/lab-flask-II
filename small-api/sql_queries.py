from sql_connection import engine

import pandas as pd
# import sys
# sys.path.append('/.../configg/sql_connection.py')
import sql_connection as dfdfd

def get_everything_():
    query = f"SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")



def table_ten(table_name):
    # select 10 rows from the specified table
    query = f"SELECT * FROM {table_name} LIMIT 10;"
    
    # execute the query and save the results to a Pandas dataframe
    df = pd.read_sql(query, engine)
    
    # return the dataframe
    return df
