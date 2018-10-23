#Desempaquetando una lista de argumentos

lista = list(range(3, 6)) #Llamada normal con argumentos
print(lista)

args = [4, 6]

lista2 = list(range(*args)) #Llamada con argumentos desmpaquetados de la lista
print(lista2)

print("Argumentos nombrados con operador **::")

def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

    #Argumentos nombrados con operador **::

d = {'tension': 'cinco mil', 'estado': 'demacrado', 'accion':'volar'}
loro(**d)