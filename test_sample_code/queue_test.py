from queue import Queue

q = Queue()
q.put(2)
q.put(3)
q.put(7)

a = q.get()
b = q.get()
c = a+b
print(c)
