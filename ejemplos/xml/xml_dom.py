#Test xml.dom

from xml.dom import minidom

doc = minidom.parse('NEWSELUJA_queries_spanish.xml')
#print(doc.toxml()) #Sacamos todo el xml

#Referencia directa

nodos = doc.childNodes
#print(nodos[0].toxml()) #Me devuelve todos los hijos

#Busca y lee el Tag seleccionado y todos sus hijos

for nodo in doc.getElementsByTagName('query')[:2]:
    print(nodo.toxml())

