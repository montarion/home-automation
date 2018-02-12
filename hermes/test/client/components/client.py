from socket import *
from time import sleep

class discovery:
    def __init__(self):
        pass

    def sendprobe(self, q1):
        while True:
            try:
                msg = q1.get(False)     # False makes it non-blocking, but raises an except 
            except:                     # on emptry queue
                msg = None

            if (msg == 'UDP DONE'):
                break



            dest = ('<broadcast>')
            port = 13000
            addr = (dest, port)


            BSock = socket(AF_INET, SOCK_DGRAM)
            BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
            BSock.sendto(bytes('marco', "utf-8"), addr)
            print('PROBE SENT.')
            sleep(1)
            BSock.close()




    def listen(self, q1):
        host = ""
        port = 13001
        buf = 1024
        #result_queue.put('already here!')
        addr = ((host, port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        UDPSock.bind(addr)
        print('waiting for server')
        (data, ipaddr) = UDPSock.recvfrom(buf)
        print('got the deets')
        print(str(ipaddr[0]), 'says', str(data)[2:-1])
        q1.put('UDP DONE')



