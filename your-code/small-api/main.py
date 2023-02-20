import requests
import random
from flask import Flask, request, jsonify
import tools.sql_queries as sql

app = Flask(__name__)
@app.route("/hello_world")
def hello_world():
    return f"Hello world!"

@app.route("/random")
def random_int():
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything())

@app.route("/table/<table>")
def table_ten (table):
    return jsonify(sql.table_ten(table))

if __name__ == "__main__":
    app.run(port=7070, debug=True)


