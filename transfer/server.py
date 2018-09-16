import socket
import threading

host = 'localhost'
port = 61234

def recv_image(ct):
    fname = ct.recv(1000).decode()
    print('incoming image name is',fname)
    f = open('new_'+fname+'.jpg','wb')
    while True:
        data = ct.recv(100)
        if data == ''.encode() or data == 'hello'.encode():
            print('Receive image successfully!')
            break
        f.write(data)
    f.close()

def listen(ct):
    while True:
        data = ct.recv(100).decode()
        if data == 'quit' or data == '':
            print('Yout friend quits the chat room')
            break
        elif data == 'send_image':
            recv_image(ct)
        else:
            print(data)

def write(ct):
    while True:
        data = input()
        ct.sendall(data.encode())
        if(data=='quit'):
            break

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sr:
        sr.bind((host,port))
        sr.listen()
        while True:
            print("Waiting to connect with...")
            ct,addr = sr.accept()
            print("Connected with",addr)
            ls = threading.Thread(target=listen,args=(ct,))
            wt = threading.Thread(target=write,args = (ct,))
            ls.start()
            wt.start()       
            ls.join()
            wt.join()
            print("Disconnected with",addr)
        sr.close()

            
            
if __name__ == '__main__':
    main()
