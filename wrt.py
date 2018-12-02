import fun
import time
import socket
HOST = 'localhost'
PORT = 9999
ct = socket.socket()
ct.connect((HOST,PORT))


def write():
    msg = (input()+'\n').encode()
    bits = fun.tobits(msg)
    ff = fun.toframe(bits)
    for i in ff:
        ct.sendall(i)
        time.sleep(0.11)    


while True:
    write()







