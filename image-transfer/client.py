import os
import socket

addr = ('localhost',63000)

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sr:
        sr.bind(addr)
        sr.listen(2)
        f = open('data_base.jpg','wb')
        while True:
            print("Waiting to connect...")
            ct,ct_addr = sr.accept()
            print('Connected with',ct_addr)
            i = 1
            while True:
                i += 1
                data = ct.recv(100)
                if not data:
                    print('done!',i)
                    break
                f.write(data)
            ct.close()

if __name__ == '__main__':
    main()
