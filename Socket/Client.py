import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        recData=s.recv(1024).decode()
        print('server: ',recData)
        sendData=input('Client: ')
        s.send(bytes(sendData,'utf-8'))
        print('Data Sent')
s.close()