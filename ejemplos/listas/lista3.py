#Compresión de listas
""" 
    cuadrados = []
    for x in range(10): 
    cuadrados.append(x**2)
"""              
cuadrados = [x ** 2 for x in range(10)]
print("Primera Lista", cuadrados)
print("\n")

#lista de compresión
combs = [(x,y) for x in (1, 2, 3) for y in (5, 1, 4) if x != y]
print("segunda lista", combs)
print("\n")

