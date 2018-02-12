from components.server import probe
from components.tcpserver import receive
import os

if not os.path.exists('dictionary.txt'):
    menu = 'probe'

while True:
    menu  = input('what do you want to do? ')

    if menu == '1':
        msg = 'received'
        receive().receive(msg)

    if menu == '2' or menu == 'probe':
        devices = '1'             #changing this because the system can't handle more than 1 node at a time anyway
        probe().start(devices)

    if menu == 'help':
        print("your options are: \n1: to use standard operation. \n2: for first time setup, or to add a new node.")


