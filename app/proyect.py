from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
	tit="tipulo pagina 1\n"
	return tit

@app.route("/data")
def data():
	return jsonify({'data': 2})
	
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
