from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = '''
    SELECT *
        from salaries
        LIMIT 10;
    '''
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (one_table):
    query = f'''
    SELECT *
        from {one_table}
        LIMIT 10;
    '''
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')