def fib(n):  # escribe la serie 
    """ comentario """
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b

    """cuidado con identar!"""

f = fib #Renombarmos la función
f(2000)