class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad 
    def __repr__(self):
        return f"{self.nombre} (Fuerza : {self.fuerza}, velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre= self.nombre + "-" + otro_pj.nombre
        nuevo_fuerza= ((self.fuerza + otro_pj.fuerza)/2)**2
        nuevo_velocidad=((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre,nuevo_fuerza,nuevo_velocidad)
    
goku=Personaje("Goku",12222,331313)
vegeta=Personaje("Vegeta",11000,20010)

gogeta = goku + vegeta
print(gogeta)