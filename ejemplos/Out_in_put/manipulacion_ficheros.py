#En este ejpmlo vamos a convetir 

import os

#Creamos un árbol de directorios

lista_lineas = []
structuredLine = []
with open('qrels.txt') as file:
    #print(file.readline())
    for line in file:
        #Hacemos una lista de cadenas separadas por split
        structuredLine = line.split()
        if(structuredLine[1]  != '0'):
            lista_lineas.append(structuredLine)
            
    #Saca la posición 0 de la lista print(lista_lineas[0])       
    #print(lista_lineas[1][0])
#print(lista_lineas)
#Vamos a crear un árbol de directorios

i = 1

if os.path.exists('data'):
    print("El árbol de directorios ya existe")
else:
    os.mkdir('data')
    while i < 21:
        if i < 10:
          os.mkdir('data/' + 'Q00' + str(i))
        if i in range(10, 21):
            os.mkdir('data/' + 'Q0'  + str(i))
        i += 1

list_dir = os.listdir('data/')
#print("list_dir", sorted(list_dir))
directorios = []

for directorio in list_dir:
    directorios.append(directorio.split('Q'))
    directorios = sorted(directorios)

#print("directorios",directorios[0][1])
#print(directorios)

#Se compara el num de la lista de lineas y el de directorios

contador_lineas = 0
contador_directorio = 0
contadorconsultas = 0

print(len(lista_lineas), len(directorios))

while contador_lineas < len(lista_lineas):
    if lista_lineas[contador_lineas][0] == directorios[contador_directorio][1]:
        print("Linea", lista_lineas[contador_lineas][0], "directorio", directorios[contador_directorio][1], "tiene misma consulta")
        contador_lineas += 1
        # if contador_lineas < len(lista_lineas)
    else: 
        print("Linea", lista_lineas[contador_lineas][0], "directorio", directorios[contador_directorio][1], "No coincide")
        if contador_directorio < len(directorios):
            #print("SEgundo else", contador_directorio)
            contador_directorio += 1
        else:
            #print("SEgundo else", contador_directorio)
            contador_directorio  = 0
