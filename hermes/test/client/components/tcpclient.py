from socket import *

class journey():
    def __init__(self):
        pass

    def tcpcon(self, ipaddr, portnumber, q2, q101):
        print('tcping!')
        host = ipaddr
        port = portnumber
        address = (host, port)
        TCPSock = socket(AF_INET, SOCK_STREAM)
        print('using: ' + str(address))
        TCPSock.connect(address)

        while True:
            print('waiting for q2..')
            data = q2.get()
            TCPSock.send(bytes(str(data), encoding="utf8"))
            q101.put('just sent: ' + str(data) + ' to: ' + str(host))

