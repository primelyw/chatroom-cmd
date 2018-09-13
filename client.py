import socket
import threading

host = 'localhost'
port = 63000

def listen(ct):
    while True:
        data = ct.recv(1000).decode()
        if data == 'quit':
            print('Yout friend quits the chat room')
            break
        else:
            print(data)

def write(ct):
    while True:
        data = input().encode()
        ct.sendall(data)
        if data =='quit':
            break

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ct:
        ls = threading.Thread(target = listen,args = (ct,))
        wt = threading.Thread(target= write,args= (ct,))
        ct.connect((host,port))
        ls.start()
        wt.start()
        ls.join()
        wt.join()
        ct.close()

if __name__ == '__main__':
    main()
