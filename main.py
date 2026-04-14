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
   3 .- Simular Inversion (En Desarrollo)
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

def miportafolio():
  total = 0
  print("\n ---Mi Portafolio---")
  for f in misfondos:
     print(f"Fondo: {f.nombre} | Saldo Actual: ${f.saldo}")
     total += f.saldo
  print(f"El Saldo total de su portafolio es de : ${total} \n")

def simular_inversion():
   nombre = input("Ingrese nombre de fondo a simular: ")
   for f in misfondos:
      pass # En Desarrollo
      

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
      break
   else:
      print("Porfavor, ingrese una opcion valida. \n")
