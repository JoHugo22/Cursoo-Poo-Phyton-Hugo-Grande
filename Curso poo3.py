class Celular:
    def __init__(self, marca, modelo, camara):
      self.modelo = modelo 
      self.marca= marca
      self.camara= camara
  

    def llamar(self):
      print(f"Estas haciendo una llamada a tu amigo desde un: {self.modelo}")
  
  
    def cortar(self):
      print(f"Cortastes la llamada desde tu: {self.marca}")
      

celular1= Celular("samsung","S23","48Mp")
celular2= Celular("POCO","X5pro","68Mp")

celular1.cortar()
celular2.llamar()

