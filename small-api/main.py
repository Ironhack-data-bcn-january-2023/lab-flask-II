from flask import Flask, request, jsonify
app = Flask(__name__)
import random
import tools.sql_queries as sqll

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_number ():
   
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return jsonify(sqll.get_everything())

@app.route("/table/<one_table>")
def tabletable (one_table):
    return jsonify(sqll.table_ten(one_table))

if __name__ == "__main__":
     app.run(port=7070, debug=True)