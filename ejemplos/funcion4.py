#argumentos de las funciones
def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

"""
loro(1000)
print("\n")
loro(tension=300)
print("\n")
loro(tension=245, accion = 'Vooooom')
"""
# no debe:
# faltar argumento obligatorio, duplicar, introducir argumento desconocido
# y un argumento posicional después de uno nombrado