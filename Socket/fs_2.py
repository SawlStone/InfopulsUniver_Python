__author__ = 'Sawl_Stone'

import socket
import datetime
now_time = datetime.datetime.now()

def main():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind(('', 3333))
    serversock.listen(5) #open socket na listen, "5" - razmer ocheredi
    while (True):
        clientsock, addr = serversock.accept() # accept blokiruet rabotu, poka net zaprosa
        requestFromClient = clientsock.recv(1024).decode()
        requestFromClient = requestFromClient + " answer from server" + str(addr)
        clientsock.send(requestFromClient.encode())
        clientsock.close()

main()