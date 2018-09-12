import socket

host = 'localhost'
port = 64000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ct:
    ct.connect((host,port))
    d1 = input()
    d2 = input()
    ct.sendall(d1.encode())
    ct.sendall(d2.encode())
    rt = ct.recv(100).decode()
    print('%d + %d = %d'%(int(d1),int(d2),int(rt)))
