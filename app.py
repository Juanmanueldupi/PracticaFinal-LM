import requests
import os
from flask import Flask, render_template,abort
app = Flask(__name__)	
URL_BASE="https://phonevalidation.abstractapi.com/v1/"

@app.route('/',methods=["GET","POST"])
def inicio():
    key=os.environ["key"]
    payload = {'key':key}
    r=requests.get(URL_BASE+'x',params=payload)
    if r.status_code == 200:
	    doc=r.json()
        return render_template("inicio.html", lista=doc['x'])
    else:
        abort(404)
port=os.environ["PORT"]
app.run('0.0.0.0',  int(port), debug=False)