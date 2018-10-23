#Test xml.etree.Element

import xml.etree.ElementTree as ET
ruta_xml = 'NEWSELUJA_queries_spanish.xml'

#Se llama al xml
arbol = ET.parse(ruta_xml)
root  = arbol.getroot()
#root  = ET.fromstring(ruta_xml) NO SE COMO FUNCIONA
print('-' * 40)

#Busca todos los <query>

"""
for query in root.findall('query'):
    num      = query.find('num').text  #Saca los textos de <num>
    eliminar = query.get('eliminar')   #Busca dentro de la misma etiqueta un atributo "elimnar"
    print(num, eliminar)
"""
