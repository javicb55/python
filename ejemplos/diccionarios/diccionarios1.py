#Técnicas de Iteración + diccionarios

import math

#Items()
caballeros = dict(Legolas = 'Bosque negro', Aragorn = 'Gondor', Gimli = 'Montañas Nubladas')
for x , y in caballeros.items(): #Iteración con varios valores, metodo items()
    print("x es la Clave", x, "y es el Valor", y)

print("-" * 40)

#Enumerate()
for i in enumerate(caballeros.keys()): #por defecto saca las claves
    print(i)

print("-" * 40)

#zip()
personajes = caballeros.keys() 
lugares    = caballeros.values()

for personaje, lugar in zip(personajes, lugares):
    print("personaje {0} --> región {1}".format(personaje, lugar)) #Formateando un print

print("-" * 40)

#reversed solo con secuencias(numerales)
for x in reversed(range(1, 10, 2)):
    print(x)

print("-" * 40)

#sorted() devuelve una lista ordenada sin tocar la original

for personaje in sorted(personajes):
    print(personaje)

print("-" * 40)
#crear una nueva lista apartir de otra
datos = [56.2, float('Nan'), 35.1, float('NaN'), 123.23]
datos_filtrados = []

for valor in datos:
    if not math.isnan(valor):
        datos_filtrados.append(valor)

print(datos_filtrados)