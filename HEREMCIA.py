class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre= nombre
        self.edad=edad
        self.nacionalidad=nacionalidad


class Empleados(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

roberto= Empleados("Roberto",23,"ecuatoriano","programador",1000)

print(roberto.trabajo)