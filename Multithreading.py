import threading, queue
from threading import Lock

mylock = Lock()
p = print

def print(*a, **b):
	with mylock:
		p(*a, **b)

item = queue.Queue()

def get_from_queue():
    while True:
        print ('Число : %s\t' % (item.get()))

def put_to_queue():
    for x in range(100000000): item.put(x)

p0 = threading.Thread(target=put_to_queue, name="t0")
p1 = threading.Thread(target=get_from_queue, name="t1")
p2 = threading.Thread(target=get_from_queue, name="t2")
p3 = threading.Thread(target=get_from_queue, name="t3")
#p4 = threading.Thread(target=get_from_queue, name="t4")

#Запуск потоков в качестве демонов
#p1.setDaemon(True)
#p2.setDaemon(True)
#p3.setDaemon(True)
#p4.setDaemon(True)

p0.start()
p1.start()
p2.start()
p3.start()
#p4.start()

#Ожидание прерывания потоков
#p1.join()
#p2.join()
#p3.join()
#p4.join()
