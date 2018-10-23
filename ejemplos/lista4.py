#lista vectorial

vec = [-4, -2, 0, 2, 4]

vec2 = [x ** 2 for x in vec] 

print("Lista multiplicada por 2 ", vec2)

vec_sin_negativos = [x for x in vec if x >= 0]

print("Lista negativos", vec_sin_negativos)

#añadimos funcion

vec_función = [abs(x) for x in vec]
print("añadimos una funcion ", vec_función)

#Lista frutas

frutas = ['banana', 'manzana', 'pera']

frutasUp = [fruta.upper() for fruta in frutas] #función para todos los elementos de un array de cadenas

print("función para todos los elementos de una lista de cadenas", frutasUp)

#tuplas de dos
vec_numero_cudadrado = [(x, x ** 2) for x in range(6)] #la tupla x, x ** 2 debe de estar entre paréntesis
print("Vectores de un número y su cuadrado", vec_numero_cudadrado) #Lista de tuplas

#Aplanar una lista usando compresión de listas
vec_triple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
aplanar_vec__triple = [num for elem in vec_triple for num in elem]
print("Aplanamos vector triple", aplanar_vec__triple)
