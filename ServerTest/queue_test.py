import queue
import threading

message = queue.Queue(10)

def producter(i):
	while True:
		message.put(i)

def consumer(i):
	while True:
		message.get()

for i in range(5):
	w = threading.Thread(target=producter,args=(i,))
	w.start()

for i in range(2):
	w = threading.Thread(target=consumer,args=(i,))
	w.start()
