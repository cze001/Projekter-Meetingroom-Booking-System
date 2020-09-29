import socket
import time
import os
from progress.bar import IncrementalBar

HOST = 0
PORT = 6969



textfile = open('device_list.txt', 'r+')
IP_LIST = textfile.read().split(',')

num = 0
IP_DICT = {}


for IP in IP_LIST:
    if len(IP) > 2:
        print('Data funnet i device_list.txt, henter')
        for IP in IP_LIST:
            num += 1
            print(num, '. enhet funnet I IP-Adresse liste: ', IP)
            IP_DICT[str(num)] = IP
        IP_SELECT = input('Hvilken enhet vil du koble til?: ')
        HOST = IP_DICT.get(IP_SELECT).replace("''", '')


for IP in IP_LIST:
    if len(IP) == 1:
        HOST = IP




def FindServer():
        with IncrementalBar('Skanner etter møteroms enhet', fill='#', max=254) as bar:
            for IPSCAN in range(1,254):
                bar.next()
                try: 
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    hostip = socket.gethostbyname(socket.gethostname()) 
                    address = hostip.rsplit('.',  1)[0] + '.' + str(IPSCAN)
                    s.connect((address, 7070))
                    
                    scananswer = s.recv(1024)
                    
                    if len(scananswer.decode()) > 2:
                        global HOST
                        HOST = address
                        bar.finish()
                        print('Enhet funnet: ', scananswer.decode())
                        textfile.write(str(address))
                        break


                    
                except socket.timeout:
                    continue
                    

def ChangeMode(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        unit = s.recv(1024) 
        print("Connected successfully to", unit.decode())
        select = input('''
        1. Sett modus til utilpgjengelig
        2. Sett modus til tilgjengelig
        : ''')
        if '1' in select:
            s.send('1'.encode())
            print('Svar fra enhet:', s.recv(1024).decode())
        if '2' in select:
            s.send('2'.encode())
            print('Svar fra enhet:', s.recv(1024).decode())

for IP in IP_LIST:
    if len(IP) == 0:
        FindServer()

try:
    ChangeMode()
except ConnectionRefusedError():
    print('Tilkobling til tjener: ', IP, 'nektet. Vennligst prøv en annen IP-Adresse \n')
    time.sleep(1)