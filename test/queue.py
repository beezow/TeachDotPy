import queue

queue = queue.Queue()

queue.put(2)
queue.put(3)
queue.put(7)
queue.put(11)
queue.put(13)
queue.put(72)

print(queue.queue)

queue.get()
temp = queue.get()
queue.get()
queue.put(temp)

