#Escribir archivos

import os

with open('texto.txt', 'rb+') as f:
    #Con cadena simple
    cadena = b"Primera linea que escribo \n"
    
    f.write(cadena) # esto sobreescribe el contenido previo
    print("Primera linea")
    
    f.write(b"segunda cadena \n")
    print("Segunda linea acoplada")
    

    #con un conjunto
    """
    tupla  = ("Primer valor", 42) 
    s = str(tupla) #transoformamos la tupla a str
    f.write(s)
    print("tupla", f.write(s))
    """
    print("Devuelve la posición actual en el archivo", f.tell())

    #seek cambia la posición del objeto archivo
    f.seek(5, 2) #solo funciona con bytes
    print(f.tell()) #ahora mismo es 5
   

    


