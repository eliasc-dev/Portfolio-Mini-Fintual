class Fondo:
   def __init__(self, nombre, saldo):
      self.nombre = nombre
      self.saldo = saldo

   def simular(self, tasa, meses):
      resultado = self.saldo*(1+tasa)**meses
      return resultado

misfondos = []
total = 0

fondovacaciones = Fondo("Vacaciones", 1000)
fondoahorrocasa = Fondo("AhorroCasa", 20000)

misfondos.append(fondovacaciones)
misfondos.append(fondoahorrocasa)

print("---Mi Portafolio---")
for f in misfondos:
   print(f"Fondo: {f.nombre} | Saldo Actual: ${f.saldo}")
   total += f.saldo
print(f"El Saldo total de su portafolio es de : ${total}")