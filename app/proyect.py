from flask import Flask, jsonify
from mongo_db import mongo_db
dbname = mongo_db()

app = Flask(__name__)

@app.route("/")
def home():
	tit="titulo pagina 1\n"
	return tit

@app.route("/data")
def data():
	success = dbname.getAll()
	return success

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
