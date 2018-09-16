import socket
import threading
import struct

host = 'localhost'
port = 61234

def listen(ct):
    while True:
        data = ct.recv(1000).decode()
        if data == 'quit':
            print('Yout friend quits the chat room')
            break
        else:
            print(data)

def send_image(ct,fname):
    f = open(fname,'rb')
    while True:
        data = f.read(100)
        ct.sendall(data)
        if not data:
            break
    f.close()
    #ct.sendall('lywdone'.encode())
    print('Sending image successfully!')


def write(ct):
    while True:
        data = input()
        ct.sendall(data.encode())
        if data =='quit':
            break
        elif data == 'send_image':
            fname = input('Image path:')
            ct.sendall(fname.encode())
            send_image(ct,fname)

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ct:
        ls = threading.Thread(target = listen,args = (ct,))
        wt = threading.Thread(target= write,args= (ct,))
        ct.connect((host,port))
        ls.start()
        wt.start()
        ls.join()
        wt.join()

if __name__ == '__main__':
    main()
