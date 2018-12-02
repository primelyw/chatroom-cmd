import fun
import socket
HOST = 'localhost'
PORT = 10001
ct = socket.socket()
ct.connect((HOST,PORT))



def listen():
    info = ct.recv(256)
    ls = fun.find_sub(info,fun.TAG)
    #print(ls)
    if len(ls) == 2:
        info = info[ls[0]+len(fun.TAG)+len(fun.CRT):ls[1]]
        info = fun.unframe(info)
        #print(info)
        info = fun.get_msg(info)
        print(info,end = '')

while True:
    listen()
    










