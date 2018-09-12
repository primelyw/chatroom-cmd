import socket

host = 'localhost'
port = 64000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sr:
    sr.bind((host,port))
    sr.listen(5)
    while True:
        print("Waiting to connect with...")
        ct,addr = sr.accept()
        print(addr)
        with ct:
            while True:
                d1 = ct.recv(100).decode()
                d2 = ct.recv(100).decode()
                if not d1:
                    break
                rep = int(d1)+int(d2)
                ct.sendall(str(rep).encode())
                print('Disconnect with',addr)
            
            
