from flask import Flask, request, jsonify
import random
from tools.sql_queries import *

app = Flask(__name__)

@app.route('/')
def hello_world ():
    return 'Hello world!'

@app.route('/random_number')
def random_int ():
    return str(random.randint(0,10))

@app.route('/everything-employees')
def example():
    return jsonify(get_everything())

@app.route('/table/<one_table>')
def any_table(one_table):
    return jsonify(table_ten(one_table))

if __name__ == '__main__':
    app.run(port = 9000, debug = True)