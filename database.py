import json
from models import Fondo

def guardardatos(misfondos):
      misfondosjson = []
      for fondo in misfondos:
         misfondosjson.append(fondo.__dict__)
      with open ("fondos.json", "w") as archivo:
         json.dump(misfondosjson, archivo, indent=4)

def cargar_datos(misfondos):
   try:
     with open('fondos.json', 'r', encoding='utf-8') as archivo:
      datos_cargados = json.load(archivo)
      misfondos.clear()
      for dato in datos_cargados:
         nuevo_fondo = Fondo(dato["nombre"], dato["saldo"])      
         misfondos.append(nuevo_fondo)
   except FileNotFoundError:
      pass
