#Lista de argumentos arbitrarios

def concatenar(*args, sep="/"):
    return print(sep.join(args))
 
concatenar("tierra","marte","venus", sep="?")
