import requests
import json
import os
from flask import Flask, render_template,abort
app = Flask(__name__)	
URL_BASE="https://phonevalidation.abstractapi.com/v1/"

#Antes de poder importar key tenemos que introducir en la terminal:
#export api_key=<api_key>
key=os.environ["api_key"]

print ("Formato valido: pefijo+numero; Ej:34123456789")
phone= input("Introduce tu numero de telefono:")
payload = {'api_key':key , 'phone':phone}

r=requests.get(URL_BASE,params=payload)

if r.status_code == 200:
    doc=r.json()
    print (doc)
else:
    print ("Error, el telefono no es valido")


