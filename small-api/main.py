from flask import Flask, request, jsonify
import random
from tools import sql_queries as sql

app = Flask (__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0,10))


@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything_table())

@app.route("/table/<one_table>")
def get_one_table (one_table):
    return jsonify(sql.table_ten(one_table))



if __name__ == '__main__':
    app.run(port=9000, debug=True)