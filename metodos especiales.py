class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f"Persona(nombre: {self.nombre}, edad = {self.edad})"
    
dalto=Persona("Juan",23)

print(dalto)