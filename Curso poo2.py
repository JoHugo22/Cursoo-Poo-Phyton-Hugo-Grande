class Celular:
   def __init__(self, marca, modelo, camara):
      self.modelo = modelo + " HOLA"
      self.marca= marca
      self.camara= camara

celular1= Celular("samsung","S23","48Mp")
celular2= Celular("POCO","X5pro","68Mp")

print(celular2.marca)
print(celular2.modelo)

