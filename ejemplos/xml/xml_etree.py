#usamos la libreria etree.ElementTree

import xml.etree.ElementTree as ET
import json

tree = ET.parse('NEWSELUJA_queries_spanish.xml')
root = tree.getroot()
listaConsultas = []
print()
#lista_diccionario_etiquetas = list()
#lista_diccionario_valores   = list()

for child in root[:2]:
    #print(child.tag) todos los hijos
    query = child
    dic = {}
    for neighbor in query:
        #print(neighbor.tag, neighbor.text) sacamos los nietos de root
        #lista_diccionario_etiquetas.append(neighbor.tag)
        dic[neighbor.tag] = neighbor.text
        #lista_diccionario_valores.append(neighbor.text)
    listaConsultas.append(dic)
    #print(dic)
#print(listaConsultas)

j_son_listaConsultas = json.dumps(listaConsultas, ensure_ascii=False).encode("utf8")
print(j_son_listaConsultas)


#print(lista_diccionario_etiquetas)
#print('-' * 40)
#print(lista_diccionario_valores)
#print('-' * 40)

#Junto en una matriz
#diccionario = dict(zip(lista_diccionario_etiquetas, lista_diccionario_valores))
#print(diccionario.values())