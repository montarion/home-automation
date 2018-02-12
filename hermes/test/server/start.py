from components.server import discover
from components.tcpserver import tcpcon
from time import sleep

clientlist = {}

print(len(clientlist))
def portnumber():
    number = len(clientlist)
    base = 14010
    targetport = base + number
    return targetport


ipaddr = discover().listen()
clientlist.update(ipaddr=portnumber())
print(clientlist)

discover().send(ipaddr, portnumber())
print('opening tcp')
tcpcon().accept(portnumber())
