import flask
from flask import Flask, request, jsonify
import random
import tools.sql_queries as eseyqele

# your code here
app = Flask(__name__)



@app.route("/")
def hello_world ():
    return f"Hello World"

@app.route("/random-number")
def random_int():
     return str(random.randint(0, 10))

@app.route("/everything.employees")
def example()
     data = get_everything()
     response = jsonify(data.to_dict(orient='records'))
     return response
from flask import Flask, jsonify
from sql_queries import table_ten


@app.route('/table/<one_table>')
def select_ten(one_table):
    # call the table_ten function to select 10 rows from the specified table
    data = table_ten(one_table)
    
    # stringify the dataframe and return the result as a JSON response
    response = jsonify(data.to_dict(orient='records'))
    
    return response


if __name__ == "__main__":
     app.run(port=8123, debug= True)