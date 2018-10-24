#Manejo Excepciones
import sys

try:
    f = open("miArchivo.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Error OS: {0}".format(err))
except ValueError:
    print("No puede convertir el dato en un entero")
except:
    print("Error inesperado: ", sys.exc_info() [0])
    raise