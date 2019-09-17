from flask import Flask, Response
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
	f = open("page.html").read()
	return Response(f, mimetype='text/html')

@app.route("/test/", methods = ['POST'])
def hello4():
	return "rishabh"


if __name__ == "__main__":
	app.run(host= '0.0.0.0', port=8000)