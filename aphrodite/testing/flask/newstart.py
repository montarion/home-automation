from components.server import probe
from components.tcpserver import receive
from components.webserver import webserver
import os
from time import sleep
from multiprocessing import Process


menu = input('hey')

try:
    if menu == '1':
        print('starting tcp server')
        def tcp():
            msg = 'received'
            global pid1
            pid1 = os.getpid()
            receive().receive(msg)

        os.environ['LC_ALL'] = 'C.UTF-8'
        os.environ['LANG'] = 'C.UTF-8'

        print('start webserver')
        def web():
            global pid2
            pid2 = os.getpid()
            webserver().runserver()
        p1 = Process(target=tcp)
        p1.start()
        
        while True:
            p2 = Process(target=web)
            p2.start()
            sleep(10)
            p2.terminate()
            
except KeyboardInterrupt:
    os.system('kill ' + pid1 + ' && kill ' + pid2)

if menu == '2' or menu == 'probe':
    devices = '1'             #changing this because the system can't handle more than 1 node at a time anyway
    probe().start(devices)
