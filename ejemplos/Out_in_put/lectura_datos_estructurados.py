#Numeros

with open('numeros.txt') as n:
    lectura_primera_linea = n.readline()
    print("Lo lee como cadena", type(lectura_primera_linea))
    casteo_primera_linea  = int(lectura_primera_linea)
    print("Caseto de la línea a número ", type(casteo_primera_linea))


print('-' * 40)

