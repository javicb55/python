#Matrices

matriz = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11)
]

print("Matriz madre", matriz)

#trasponemos las filas y las columnas
matriz_t = [[fila[i] for fila in matriz] for i in range(4)]

print("Matriz traspuesta", matriz_t)

#es lo mismo que
matriz_t2 = []
for i in range(4):
    matriz_t2.append([fila[i] for fila in matriz])
print("Traspuesta 2", matriz_t2)

#y es lo mismo a:
matriz_t3 = []
for i in range(4):
    # Compresión de filas anidadas
    fila_traspuesta = []
    for fila in matriz:
        fila_traspuesta.append(fila[i])
    matriz_t3.append(fila_traspuesta)
print("Traspuesta 3", matriz_t3)
    
#Con la función zip
matriz_a_partir_funcion = list(zip(*matriz))
print("función zip", matriz_a_partir_funcion)