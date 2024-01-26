class Gato:
    def sonido(self):
        return"Miau"
    
class Perro:
    def sonido(self):
        return"Guau"

gato=Gato()
perro=Perro()

print(gato.sonido())
print(perro.sonido())

#otro ejemplo

def recorre(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

Lita={1,2,3,4}
lista2="Hugo"

recorre(Lita)
recorre(lista2)