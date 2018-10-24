"""
a = 1 #Los valores son evaludados en el momento de la función

def f(args = a):
    print(args)

a = 2

funcion1()
"""

# Excepto si es mutable
def lista(a, L=[]): 
    L.append(a)
    return L
print(lista(1))
print(lista(2))
print(lista(3))

# valor [1], [1,2], [1,2,3]