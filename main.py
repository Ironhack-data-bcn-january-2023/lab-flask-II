from flask import Flask
from flask import jsonify
import small_api.tools.sql_queries as sql

import random

app = Flask(__name__)


@app.route("/hello-world")
def hello ():
    return f"Hello world!"


@app.route("/random/<therange>")
def random_number (therange):
    therange = int(therange)
    return str(random.randint(0, therange))


@app.route("/table/everything-employees")
def get_everything_table ():
    return jsonify(sql.get_everything_table())

@app.route("/table/<one_table>")
def table_ten (table_q):
    return jsonify(sql.table_ten(table_q))


app.run(port=51814 , debug=True)