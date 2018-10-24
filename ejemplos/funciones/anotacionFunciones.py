def f(lechuga: str, perros:str = 'perros')-> str:
    print("Anotaciones:", f.__annotations__)
    print("Anotaciones", lechuga,perros)
    return print(lechuga + " y " + perros)


f('macarrones')
