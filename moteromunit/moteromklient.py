import socket
from sys import excepthook
import time
import cv2
import numpy as np

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969     
NAME = 'Moteroms-klient 1'
print('Møteromklient starter nå på IP:', HOST, '\nPort:',PORT)

try:
    time.sleep(1)
    print('\nTester find_device broadcast')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 7070))

except ConnectionRefusedError:
    print('Klarte ikke å finne find_device broadcast. Dette kan skape problemer for moteromkontroll.exe. Lag eventuelt device_list.txt manuelt med IP Adresse til moteromenhet. PORT 6969, 7070 opp mot IP: {} må være tilgjengelig for programvare på enhet som brukes til oppkobling (Moteromkontroll.exe)'.format(HOST))
    

while True: 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        unit = NAME.encode()
        conn.send(unit)

        selection = conn.recv(1024).decode()
        if selection == '1':
            Background_Image = np.zeros((512,1024,3), np.uint8)
            status = 'Utilgjengelig'
            color = (0,0,255)
            fscale = (50, 300)
            conn.send('Suksess'.encode())
            print('Request fått fra:', addr, 'Setter status til:', status)
        if selection == '2':
            Background_Image = np.zeros((512,1024,3), np.uint8)
            status = 'Tilgjengelig'
            color = (0,255,0)
            fscale = (90, 300)
            conn.send('Suksess'.encode())
            print('Request fått fra:', addr, 'Setter status til:', status)
        moterom_status = cv2.putText(Background_Image, status, fscale, cv2.FONT_HERSHEY_SIMPLEX, 5, color, 2, cv2.LINE_AA)
        cv2.imshow('Rom-Status', moterom_status)
        cv2.waitKey(1)
        selection = conn.recv(1024).decode()
    
    except KeyboardInterrupt:
        quit()
        



            