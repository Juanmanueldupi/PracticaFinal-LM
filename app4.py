import requests
import json
import os

URL_BASE="https://pokeapi.co/api/v2/"
r=requests.get(URL_BASE+'pokemon/')
if r.status_code == 200:
    doc=r.json()
    print ("Listado de Pokemons")
    for pokemon in doc.get("results"):
        print (pokemon.get("name"))
else:
    print ("Error en la API")
        