#leer archivos

with open('texto.txt') as f: # With --> cierra el texto
    #print("Lee los primeros 20 caracteres", f.read(20)) #espacios en blancos incluidos
    """
    print(f.readline()) #devuelve la primera linea
    print(f.readline()) #devuelve la segunda linea (salto de linea)
    print(f.readline()) #Tercera línea
    print(f.readline()) #cuarta línea
    """
    
    """
    for linea in f:
        print(linea, end = '' ) #Itera y lee todo el archivo
    """
    #print(list(f)) lee en una lista las lineas del archivo
    #también se puede así print("Usando f.readlines", f.readlines())