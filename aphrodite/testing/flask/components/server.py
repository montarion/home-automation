from time import *
from socket import *

dictionary = {}
name = 'SERVER1'

#---creates id---#
class probe:
    def __init__(self):
        global base
        base = name + ":" + "SERVER" + ":"   #CODE           #1000 == DISCOVER

        pass



    def start(self, devices):
        i  = 0

        if i < eval(devices):
            def sendprobe():
                dest = ('<broadcast>')
                port = 13000
                addr = (dest, port)
                BSock = socket(AF_INET, SOCK_DGRAM)
                BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
                probe = base + '1000'
                BSock.sendto(bytes(probe, "utf-8"), addr)
                #print('PROBE SENT.')
                sleep(0.5)
                BSock.close()
            def sending(addr, code):
                print('sending code')
                sleep(2)
                port = 13000
                addr = (addr, port)
                BSock = socket(AF_INET, SOCK_DGRAM)
                BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
                #send status to client.
                BSock.sendto(bytes(code, "utf-8"), (addr))
                #print('sent', code, 'to', ip)
                BSock.close()
                done = True
                return done
            sendprobe()
            host = ""
            port = 13000
            buf = 1024
            addr = (host, port)
            UDPSock = socket(AF_INET, SOCK_DGRAM)
            UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            UDPSock.bind(addr)




            print('waiting for replies')
            (data, addr) = UDPSock.recvfrom(buf)
            print('recieved the deets')
            data = str(data)
            addr = str(addr)
            #print(data)
            if data[-5:-1] == '0001':            #CODE           #0001 == DISCack
                clientname = data[2:data.find(':')]
                #print(clientname)
                ip = addr[2:addr.find(',')-1]
                #print(ip)
                print('setting up connection with ' + data[2:data.find(':')])
                dictionary.update({data[2:data.find(':')]: addr[2:addr.find(',')-1]}                                                                                                                                                             )
                infile = open('dictionary.txt', 'w')
                infile.write(str(dictionary))
                infile.close()
                localstatus = '0002'            #CODE   #0002 == udp connected
                code = base + localstatus
                #print(clientname, addr)
                addr = ip
                sending(addr, code)
                if sending(addr, code) == True:
                    i = i + 1
                    #print(i)
                print('done.')
                #print(dictionary)
                UDPSock.close()
            #print('next')
            sleep(3)
        return dictionary
        raise SystemExit




