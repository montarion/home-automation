from components.client import discovery
from multiprocessing import Process, Queue


if __name__== '__main__':
    q1 = Queue()
    q2 = Queue() #aditional queues are possible
    t1 = Process(target=discovery().sendprobe, args=(q1,))
    p2 = Process(target=discovery().listen, args=(q1))

    p2.start()
    t1.start()
