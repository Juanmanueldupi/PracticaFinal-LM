import requests
import json
from flask import Flask, render_template,abort
app = Flask(__name__)
URL_BASE="https://pokeapi.co/api/v2/"
r=requests.get(URL_BASE+'pokemon/')
if r.status_code == 200:
    doc=r.json()
    print ("Listado de Pokemons")
    print (doc)
else:
	print("Error en la API")
