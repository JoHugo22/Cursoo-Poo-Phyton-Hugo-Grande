class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d=D()
d.hablar()

B.hablar(d)
C.hablar(d)
A.hablar(d)

print(D.mro())