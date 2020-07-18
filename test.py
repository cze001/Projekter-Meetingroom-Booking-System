import socket
import time
import os

HOST = '0'
PORT = 6969

textfile = open('device_list.txt', 'r+')
IP_LIST = textfile.read().split('.')
num = 0
IP_DICT = {}

if len(IP_LIST) > 1:
    print('Data funnet i device_list.txt, henter')
    for IP in IP_LIST:
        num += 1
        print(num, '. enhet funnet I IP-Adresse liste: ', IP)
        IP_DICT[str(num)] = IP
    IP_SELECT = input('Hvilken enhet vil du koble til?: ')
    HOST = IP_DICT.get(IP_SELECT).replace("''", '')
    print(HOST)

for IP in IP_LIST:
    if len(IP) == 1:
        HOST = IP




def FindServer():
        for IPSCAN in range(164,254):
            try: 

                os.system('cls')
                print('Finner enhet: |')
                time.sleep(0.1)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                hostip = socket.gethostbyname(socket.gethostname()) 
                os.system('cls')
                
                print('Finner enhet: /')
                time.sleep(0.1)
                address = hostip.rsplit('.',  1)[0] + '.' + str(IPSCAN)
                s.connect((address, 7070))
                os.system('cls')
                
                print('Finner enhet: —')
                time.sleep(0.1)
                scananswer = s.recv(1024)
                if len(scananswer.decode()) < 2:
                    print('Enhet funnet: ', scananswer.decode())
                    HOST = IPSCAN
                os.system('cls')

                print('Finner enhet: "\"')
                time.sleep(0.1)
                if len(scananswer.decode()) > 2:
                    HOST = address
                    print('Enhet funnet: ', scananswer.decode())
                    textfile.write(str(address))
                    break

            except socket.timeout:
                continue
                

def ChangeMode(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(HOST)
        s.connect((HOST, PORT))
        unit = s.recv(1024) 
        print("Connected successfully to", unit.decode())
        select = input('''
        1. Sett modus til utilgjengelig
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

ChangeMode()
