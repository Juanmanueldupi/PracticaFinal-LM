import requests
import json
from flask import Flask, render_template,abort
app = Flask(__name__)
URL_BASE="https://pokeapi.co/api/v2/"

pokemon=input("Introduce el numero de un pokemon: ")
payload= {'pokemon':pokemon}
r=requests.get(URL_BASE+'pokemon-form/',params=payload)


if r.status_code == 200:
    doc=r.json()
    print (doc)
else:
	print("Error en la API")
