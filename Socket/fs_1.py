__author__ = 'Sawl_Stone'

import socket

class ClientSocket:
    def __init__(self, addr, port):
        self.port = port
        self.addr = addr

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.addr, self.port)) # connect to server-port
        message = input()
        sock.send(message.encode()) # send to server
        answer = sock.recv(1024).decode() # 1024 kvota kolichestva danyx
        print(answer)
        sock.close()

def main():
    c = ClientSocket("127.0.0.1", 3333)
    c.connect()

main()
