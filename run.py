import fun
import time
import socket
import threading
HOST = 'localhost'
ct = socket.socket()


def write():
    while True:
        msg = (input()+'\n').encode()
        bits = fun.tobits(msg)
        ff = fun.toframe(bits,0)
        for i in ff:
            ct.sendall(i)
            time.sleep(0.11)

def listen():
    while True:
        info = ct.recv(256)
        ls = fun.find_sub(info,fun.TAG)
        if len(ls) == 2:
            info = info[ls[0]+len(fun.TAG)+len(fun.ACK0):ls[1]]
            info = fun.unframe(info)
            #print(info)
            info = fun.get_msg(info)
            print(info,end = '')    

if __name__ == '__main__':
    print("Please input the port")
    PORT = int(input())
    ct.connect((HOST,PORT))
    lis = threading.Thread(target=listen)
    wrt = threading.Thread(target = write)
    lis.start()
    wrt.start()










