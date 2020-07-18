import socket
from sys import excepthook
import time
import cv2
import numpy as np

HOST = '10.0.0.166'  
PORT = 7070     
NAME = 'Moteroms-klient 1'

while True: 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        unit = NAME.encode()
        conn.send(unit)
    except:
        continue