def fib2(n):
        result = []
        a, b = 0, 1
        while b < n:
                result.append(b) #Esto es igual que result = result + [b]
                a,b = b, a+b
        return result

f100 = fib2(100)        #Renombramos la función para 100 numeros
print(f100)         