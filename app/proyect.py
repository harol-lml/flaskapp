from flask import Flask, jsonify, request
from mongo_db import mongo_db
dbname = mongo_db()

app = Flask(__name__)

@app.route("/")
def home():
	tit="titulo pagina 1\n"
	return tit

@app.route("/data", methods=['GET', 'POST'])
def data():
	if request.method == 'GET':
		if(request.args):
			data = dbname.getById(request.args['id'])
			return data
		success = dbname.getAll()
		return jsonify(success)
	else:
		note = dbname.postNote(request.form)
		return (note)

@app.route("/put", methods=['PUT'])
def dataPut():
	note = {
		"content":	request.form['content'],
		"old":		request.form['old']
		}
	dbname.putNote(note)
	return jsonify(note)

@app.route("/delete", methods=['DELETE'])
def dataDelete():
	id = request.form['id']
	resp = dbname.deleteNote(id)
	return jsonify(resp)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
