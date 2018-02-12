import os
from components.client import probing
from components.tcpclient import sending

if not os.path.exists('serverip.txt'):
    ip = probing().receive()
else:
    infile = open('serverip.txt')
    ip = infile.read()


msg = 'this is client two'

sending().sendmsg(str(ip), msg)
