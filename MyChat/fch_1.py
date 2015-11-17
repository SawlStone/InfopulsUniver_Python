__author__ = 'Sawl_Stone'

# ServerChat

import socket
import select
import threading

class ClientHandler(threading.Thread):
    def __init__(self, clientsocket, clients):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.clients = clients

    def run(self):
        name = self.clientsocket.recv(1024).decode()
        self.clients[name] = self.clientsocket
        while True:
            message = self.clientsocket.recv(1024).decode()
            if message == "list":
                answer = "list: "
                for names in self.clients.keys():
                    answer = answer + names + ":"

                self.clientsocket.send(answer.encode())
            else:
                name, messageForName = message.split(":")
                self.clients[name].send(messageForName.encode())



class ServerChat:
    def __init__(self):
        self.port = 7777
        self.clients = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self):
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(5) #odovrimennyj zapros na awtirizaciyu
        while True:
            clientsocket, addr = self.sock.accept() #perebroska na drugoj port
            select.select([clientsocket], [clientsocket], []) # 'select' - delayet socket asinhronnym
            thread = ClientHandler(clientsocket, self.clients) #potok obrabatyvaet konkretnogo clienta
            thread.start()

def main():
    server = ServerChat()
    server.bind()
main()
