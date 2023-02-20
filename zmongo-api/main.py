# BONUS
from flask import Flask, request, jsonify
import random
from mongo_tools.mongo_queries import random_filter

app = Flask(__name__)

@app.route('/')
def welcome_screen ():
    return 'This is the MongoDB exercise server!'

@app.route('/random-query')
def random_query ():
    return jsonify(random_filter())

if __name__ == '__main__':
    app.run(port = 9000, debug = True)