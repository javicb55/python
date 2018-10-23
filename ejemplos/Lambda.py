def hacer_incremento(n):
    return (lambda x: x + n)

f = hacer_incremento(3)

print(f(0))
