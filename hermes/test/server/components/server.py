from socket import *
from time import sleep

class discover:

    def __init__(self):
        pass

    def listen(self):
        host = ""
        port = 13000
        buf = 1024
        addr = ((host, port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSock.bind(addr)
        print('waiting')
        (data, ipaddr) = UDPSock.recvfrom(buf)
        print('got the deets')
        print(str(ipaddr), 'says', str(data[2:-1]))
        sleep(1)
        UDPSock.close()
        return ipaddr[0]


    def send(self, ipaddr, targetport):
        print('sending')
        host = str(ipaddr)
        port = 13001
        buf = 1024
        addr = ((host, port))
        BSock = socket(AF_INET, SOCK_DGRAM)
        BSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        message = 'polo: ' + str(targetport)
        print(message)
        print(addr)
        BSock.sendto(bytes(message, "utf-8"), addr)
        BSock.close()

