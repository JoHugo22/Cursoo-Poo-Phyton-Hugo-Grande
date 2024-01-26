class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad

    def get_nombre(seft):
        return seft.__nombre
    
    def set_nombre(seft,new_nombre):
        seft.__nombre=new_nombre


dalton=Persona("Lucas",21)

nombre= dalton.get_nombre()
print(nombre)

dalton.set_nombre("Madisson")

nombre= dalton.get_nombre()
print(nombre)
