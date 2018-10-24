frutas = ['naranja' , 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']

print(frutas.count('manzana'))  # 2 veces
print(frutas.count('autobus'))  # 0 ninguna
print(frutas.index('banana'))   # 3
print(frutas.index('banana',4)) # 6
frutas.reverse()
print(frutas) # ['banana', 'manzana', 'kiwi', 'banana', 'pera', 'manzana', 'naranja']
frutas.sort()
print(frutas) # ['banana', 'banana', 'kiwi', 'manzana', 'manzana', 'naranja', 'pera']
print(sorted(frutas))

fruta = "fruta"
print(sorted(fruta))