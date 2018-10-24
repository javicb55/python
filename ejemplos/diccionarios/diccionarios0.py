#Conjuntos: Diccionarios

dic = {'jack': 4078, 'fernando':3012} # Los diccionarios requieren llaves
dic['guido'] = 5123

print("Diccionario", dic)

#constructor dict() crea directamente eset diccionario
dic_constructor = dict(jose=4078, fernando=3012, guido=5123)
print("Constructo con dic()", dic_constructor)

#Clave valor desde compresiones

dic_numeros = {x: x ** 2 for x in (2, 4, 6)}
print("diccionario de números", dic_numeros)
print("mostrando lista de las claves", list(dic_numeros.keys()))
