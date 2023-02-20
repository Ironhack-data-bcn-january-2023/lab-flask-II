from flask import Flask, request, jsonify
import random
import config.sql_connection as engine
import tools.sql_queries as sql

app = Flask(__name__)
@app.route("/", methods=["GET"])
def hello_this_works ():
    return f"Hello world!"

@app.route("/random-number", methods=["GET"])
def random_no():
    return str(random.randint(0,10))

@app.route("/everything-employees")
def example():
    return jsonify(sql.get_everything())

@app.route("/table/<tbl>")
def table_ten(tbl):
    return jsonify(sql.tbl_tn(tbl))


if __name__ == "__main__":
    app.run(port=9000, debug=True)