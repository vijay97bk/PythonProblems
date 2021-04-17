import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        sendData=input('Server: ')
        conn.send(bytes(sendData,'utf-8'))
        recData=conn.recv(1024).decode()
        print('client: ',recData)
conn.close()