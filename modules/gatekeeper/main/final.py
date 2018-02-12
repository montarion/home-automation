##add option to add devices to file devices.txt##

import os
from time import sleep

def homefunc():
    global dictionary, adresses
    dictionary = {}

    adresses = []
    infile = open('devices.txt')
    text = infile.readlines()
    infile.close()
    i = 0
    while i < len(text):


        addrstart = 2
        endsearch = '":'
        addrend = str(text[i]).find(endsearch)
        begin2search = ':"'
        namestart = str(text[i]).find(begin2search) + 2
        dictionary.update({text[i][addrstart:addrend]:text[i][namestart:-3]})
        ip = text[i][addrstart:addrend]
        adresses.append(ip)
        i += 1

    return dictionary


def devconnected():
    print('updating devices..')
    os.system('sudo nmap -sn 192.168.178.1/24 > connected.txt')
    sleep(2)
    infile = open('connected.txt')
    convert = infile.readlines()
    infile.close()
    i = 2
    connected = []
    while i < len(convert):
        thing = convert[i]

        search = thing.find('192.168') #finds the position of common part of ip address range.
        if thing[-2]==')': # gets rid of the ')' nmap puts at the end of the ip address if the device has a name
            connected.append(thing[search:-2])
        else:
            connected.append(thing[search:-1])
        i += 3
    return connected


def alert():
    test = set(devconnected()).intersection(adresses)
    
    i = 0
    print('These are here: ')
    while i < len(test):

        print(dictionary[adresses[i]])
        i += 1


homefunc()

alert()

