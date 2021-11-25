import flask 
from flask import request,jsonify,render_template

app = flask.Flask(__name__)
app.config["DEBUG"]=True
@app.route('/')
def home():
    return render_template("DAPconsumedAPI.html")
app.run()