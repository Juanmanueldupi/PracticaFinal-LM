import requests
import json
import os

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
    print("Telefono",doc.get("phone"))
    print("valido",doc.get("valid"))
    print("Formato Internacional",doc.get("format").get("international"))
    print("Formato Local",doc.get("format").get("local"))
    print("Iniciales del Pais",doc.get("country").get("code"))
    print("Pais",doc.get("country").get("name"))
    print("Prefijo",doc.get("country").get("prefix"))
    print("Localizado en:",doc.get("location"))
    print("Tipo",doc.get("type"))
    print ("Ultima Operadora conocida",doc.get("carrier"))
else:
    print ("Error, el telefono no es valido")


