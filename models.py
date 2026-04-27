class Usuario:
   def __init__(self, nombre, saldo_disponible):
      self.nombre = nombre
      self.saldo_disponible = saldo_disponible

class Fondo:
   def __init__(self, nombre, saldo):
      self.nombre = nombre
      self.saldo = saldo

   def simular(self, tasa, meses):
      resultado = self.saldo*(1+tasa)**meses
      return resultado

