from socket import *

class receive:
    def __init__(self):
        pass

    def receive(self, msg):
        host = ""
        port = 13333
        buf = 1024
        addres = (host, port)
        TCPsock = socket(AF_INET, SOCK_STREAM)
        TCPsock.bind(addres)
        TCPsock.listen(10)
        name = 'SERVER1'
        infile = open('dictionary.txt')
        dictionary = eval(str(infile.read()))
        infile.close        
        while True:
            c, addr = TCPsock.accept()
            data = c.recv(buf)
            data = str(data)
            host = repr(addr[0])[1:-1]
                      
            print(dictionary[host] + " says: " + data[2:-1])
            # POSSIBLE message
            if msg:
                print('sending message')
                c.send(bytes(msg, "utf-8"))



