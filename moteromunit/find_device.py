import socket
from sys import excepthook


HOST = socket.gethostbyname(socket.gethostname())
PORT = 7070     
NAME = 'Moteroms-klient 1'
print ('Find_device broadcaster nå på:', HOST, '\nPort:',PORT)
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