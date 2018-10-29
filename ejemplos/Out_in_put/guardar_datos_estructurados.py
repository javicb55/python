#Json
import json

x = 1, 'simple', 'lista', 'clases'

x = json.dumps(x) #Modifica a un Json

diccionario = dict(Legolas = 'Bosque negro', Aragorn = 'Gondor', Gimli = 'Montañas Nubladas')

with open('texto.txt', 'r+') as f:
    #json.dump(diccionario, f) # Escribe el diccionario formato Json
    #No se puede lanzar un dump y luego un load

    data = json.load(f) #Solo se puede hacer load de un json bien formado
    print(data)
    

    
    
