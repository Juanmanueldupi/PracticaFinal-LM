import requests
import json
import os

URL_BASE="https://pokeapi.co/api/v2/pokemon-form/"

pokemon=input("Introduce el numero de un pokemon: ")
r=requests.get(URL_BASE+pokemon)


if r.status_code == 200:
    doc=r.json()
    print("Id:",doc.get("id"))
    print("Pokemon:",doc.get("name"))
    print("Sprite:",doc.get("sprites").get("front_default"))
else:
	print("Error en la API")