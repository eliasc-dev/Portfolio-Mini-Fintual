import json

class Fondo:
   def __init__(self, nombre, saldo):
      self.nombre = nombre
      self.saldo = saldo

   def simular(self, tasa, meses):
      resultado = self.saldo*(1+tasa)**meses
      return resultado

def menu():
   print(""" -----Mini Fintual Menu-----   
   1 .- Ver Portafolio
   2 .- Crear Nuevo Fondo  
   3 .- Simular Inversion
   4 .- Salir
         """)

misfondos = []
total = 0

fondovacaciones = Fondo("Vacaciones", 1000)
fondoahorrocasa = Fondo("AhorroCasa", 20000)

misfondos.append(fondovacaciones)
misfondos.append(fondoahorrocasa)


def crearfondo():
  nombre = input("Ingrese el nombre del fondo: ")
  try:
   saldo = float(input("Ingrese el saldo inicial para el fondo: "))
  except ValueError:
     print("\nError: El saldo debe ser un número. \n")
     return
  nuevo_fondo = Fondo(nombre, saldo)
  misfondos.append(nuevo_fondo)
  guardardatos()

def miportafolio():
  total = 0
  print("\n ---Mi Portafolio---")
  for f in misfondos:
     print(f"Fondo: {f.nombre} | Saldo Actual: ${f.saldo}")
     total += f.saldo
  print(f"El Saldo total de su portafolio es de : ${total} \n")

def simular_inversion():
   if len(misfondos) == 0:
      print("No existen fondos que simular, porfavor, cree un fondo y vuelva a intentarlo.")
   nombrefondo = input("Ingrese nombre de fondo a simular: ")
   for fondo in misfondos:
      if fondo.nombre.lower() == nombrefondo.lower():
        try:
           tasafondo = float(input("Ingrese la tasa de interes a simular: "))
        except ValueError:
           print("\nError: La tasa debe ser un número. \n")
           return
      tasareal = tasafondo/100
      try:
           mesesfondo = int(input("Ingrese los meses a simular: "))
      except ValueError:
           print("\nError: Los meses deben ser un numero. \n")
           return
      simulacion = fondo.simular(tasareal,mesesfondo)
      valor = round(simulacion, 2)
      print(f"\n- Para {mesesfondo} meses se ha simulado que su fondo tendra un valor de: ${valor} \n")
      return
   print("\nERROR: Ese fondo no existe, escriba un fondo valido.\n")

def guardardatos():
      misfondosjson = []
      for fondo in misfondos:
         misfondosjson.append(fondo.__dict__)
      with open ("fondos.json", "w") as archivo:
         json.dump(misfondosjson, archivo, indent=4)
      
while True:
   menu()
   opcion = int(input("Ingrese La Opcion Que Desee: " ))
   if opcion == 1:
      miportafolio()
   elif opcion == 2:
      crearfondo()
   elif opcion == 3:
      simular_inversion()
   elif opcion == 4:
      print("\n   Finalizando Programa... \n")
      break
   else:
      print("Porfavor, ingrese una opcion valida. \n")
