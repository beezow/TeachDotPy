from queue import *

q = Queue(maxsize = 0)

q.put(2)
q.put(3)
q.put(7)
q.put(11)
q.put(13)
q.put(72)

print(q.queue)

q.get()
temp = q.get()
q.get()
q.put(temp)
