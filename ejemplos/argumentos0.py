"""

"""
def ventadequeso(tipo, *argumentos, **palabrasclaves): #tupla de argumentos -- números de valores separadas por comas.
    print("-- ¿Tiene", tipo + "?")
    print("-- Lo siento , nos quedamos sin", tipo)
    
    for arg in argumentos:
        print(arg)
    print("-" * 40)

    for c in palabrasclaves:
        print(c, "+", palabrasclaves[c])


ventadequeso("Limburguer","Es muy liquido, sr.", "Realmente es muy muy líquido, sr",
cliente="Juan Carlos", vendedor="Javier Cansado", puesto="Venta de quesos argentinos")