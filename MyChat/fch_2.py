__author__ = 'Sawl_Stone'

#Chat

import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5.QtCore import QObject,pyqtSignal
import socket
import select

class ThreadReader(threading.Thread):
    def __init__(self, serverSocket, signal):
        threading.Thread.__init__(self)
        self.serverSocket = serverSocket
        self.signal = signal

    def run(self):
        while True:
            text = self.serverSocket.recv(1024).decode()
            self.signal.emit(text)


class ChatClient(QWidget):
    sing = pyqtSignal(str)
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("clientGui.ui")
        self.addr = "127.0.0.1"
        self.port = 7777
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.Exit.clicked.connect(Qt.qApp.quit)
        self.ui.list.clicked.connect(self.showlist)
        self.ui.send.clicked.connect(self.sendMessage)

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.connect((self.addr, self.port))
        select.select([self.serverSocket], [self.serverSocket], [])
        self.sing.connect(self.fillForm)
        thread = ThreadReader(self.serverSocket, self.sing)
        thread.start()

    def showlist(self):
        self.serverSocket.send("list".encode())

    def sendMessage(self):
        messageToSend = self.ui.sendMessage.toPlainText()
        self.serverSocket.send(messageToSend.encode())

    def fillForm(self, text):
        command = text[0:4]
        if command == "list":
            client_list = text.split(":")
            self.ui.clientsList.setText("")
            clients = ""
            for clientName in client_list:
                clients = clients + clientName + "\n"

            self.ui.clientsList.setText(clients)

        else:
            message = self.ui.messages.toPlainText()
            message = message + "\n" + text
            self.ui.messages.setText(message)

def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = ChatClient()
        window.show()
        sys.exit(app.exec_())

main()