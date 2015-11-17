__author__ = 'Sawl_Stone'
# -​*- coding: utf-8 -*​-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore
import sys

class ModalForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal) # Блокирует первую форму
        Form, Base = uic.loadUiType("modalForm.ui") # Form - класс окошка в дизайнере
        self.form = Form()
        self.form.setupUi(self)
        self.form.Exit.clicked.connect(self.close)

class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("MyForm.ui") # Form - класс окошка в дизайнере
        self.form = Form()
        self.form.setupUi(self) # связываем объект Form(окошко) с виджетами
        self.form.Exit.clicked.connect(Qt.qApp.quit) # Button "Exit"
        self.form.Ok.clicked.connect(self.on_clicked) # Button "Ok"
        self.form.ModalWindow.clicked.connect(self.on_modal)

    def on_clicked(self):
        text = self.form.textEdit.toPlainText() # введенный текст помещаем в переменную
        self.form.label.setText(text)

    def on_modal(self):
        text = self.form.textEdit.toPlainText()
        modal = ModalForm(self)
        modal.form.label.setText(text)
        modal.show() # отобразить модальное окно

def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyForm()
        window.show()
        sys.exit(app.exec_())

main()