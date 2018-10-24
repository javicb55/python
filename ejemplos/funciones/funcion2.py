#Valor por Omisión
def pedir_confirmacion(prompt, reintentos=4,queja="¡Si o no, por favor!"):
    while True:
        ok = input(prompt) #Se Abre la terminal
        if ok in ('s','S','si','Si','SI'): #palabra reservada in, comprueba que la sentecia tenga o no determinados valores
            return True
        if ok in ('n','N','no','No','NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario invalida')
        print(queja)

#pedir_confirmacion('¿Realmente quieres salir?') pasamos un argumento obligatorio
#pedir_confirmacion('¿Realmente queires salir?',1) pasamos argumento obligatorio y otro opcional
#pedir_confirmacion('¿Realmente quieres salir',1,'¿Si o no?')

