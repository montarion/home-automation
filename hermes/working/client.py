from time import *
from socket import *
import random, string

import os
global localstatus, addr, statuscode
localstatus = '0000'            #CODE
addr = '0000'                   #CODE
statuscode = '0000'             #CODE meaning go
#name = input('name?')
name = 'hawk'
base = name + ":" + "CLIENT" + ":"
def receive():
    global statuscode

    print('discovery mode activated, waiting for data')


    while True:

        host = ""
        port = 13000
        buf = 1024
        addr = ((host, port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSock.bind(addr)
        #print('waiting')
        (data, addr) = UDPSock.recvfrom(buf)
        #print('got the deets')
        UDPSock.close()
        data = str(data)
        addr = str(addr)
        ip = addr[2:addr.find(',')-1]
        #print(data)

        #--commands--#
        if data[-5:-1] == '1000':       #CODE  meaning discover
            print('probe recieved, sending reply.')
            localstatus = '0001'        #CODE  meaning disack
            #print(localstatus)
            #print('server ip adress is :', addr)
            msg = base + localstatus
            sending(msg)


        if data[-5:-1] == '0002':       #CODE  meaning udp connected
            localstatus = '0002'
            print('preliminary connection established, setting up secure connection to', ip)
            break
    return ip

def sending(msg):
    global localstatus
    if localstatus == '0002':
        os._exit()
    dest = ('<broadcast>')
    port = 13000
    addr = (dest, port)
    BSock = socket(AF_INET, SOCK_DGRAM)
    BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
    sleep(3)
    BSock.sendto(bytes(msg, "utf-8"), addr)
    #print('sending reply')
    sleep(2)
    localstatus = '0000'

    BSock.close()



receive()


