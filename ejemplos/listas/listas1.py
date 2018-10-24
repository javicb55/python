#Usaremos una lista como si fuese una cola

from collections import deque

queue = deque(["Eric", "Jhon", "Michael"])
queue.append("Terry")
queue.append("Gabriel") #entran en ultimo lugar
print(queue)
print(queue.popleft()) #Sale el indice 0 "Eric"
print(queue)