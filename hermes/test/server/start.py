from components.server import discover
from components.tcpserver import tcpcon
from time import sleep
from multiprocessing import Process, Queue




clientlist = {}


def portnumber():
    number = len(clientlist)
    base = 14010
    targetport = base + number
    return targetport

if __name__== '__main__':
    q1 = Queue()
    q2 = Queue()

    
    ipaddr = discover().listen()
    clientlist.update(ipaddr=portnumber())
    print(clientlist)

    discover().send(ipaddr, portnumber(), q1)
    print('opening tcp')
    p1 = Process(target=tcpcon().accept, args=(q1.get(),))

    p1.start()
