import socket
from sys import excepthook
import time
import cv2
import numpy as np

HOST = '10.0.0.166'  
PORT = 6969     
NAME = 'Moteroms-klient 1'

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
        if selection == '2':
            Background_Image = np.zeros((512,1024,3), np.uint8)
            status = 'Tilgjengelig'
            color = (0,255,0)
            fscale = (90, 300)
            conn.send('Suksess'.encode())
        moterom_status = cv2.putText(Background_Image, status, fscale, cv2.FONT_HERSHEY_SIMPLEX, 5, color, 2, cv2.LINE_AA)
        cv2.imshow('Rom-Status', moterom_status)
        cv2.waitKey(1)

        selection = conn.recv(1024).decode()
    
    except:
        continue
        



            