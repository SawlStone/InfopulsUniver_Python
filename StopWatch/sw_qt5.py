__author__ = 'Sawl_Stone'
# -*- coding: utf-8 -*-
#Stopwatch: The Game

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import QBasicTimer
import sys


class MyStopWatch(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("stop_watch.ui") # Form - класс окошка в дизайнере
        self.form = Form()
        self.form.setupUi(self) # связываем объект Form(окошко) с виджетами
        self.initUI()

    def initUI(self):
        self.timer = QBasicTimer()
        x = 0
        y = 0
        self.form.Start.clicked.connect(self.start) # Button "Ok"
        self.form.Stop.clicked.connect(self.stop)
        self.form.Reset.clicked.connect(self.reset)
        score = str(x) + '/' + str(y)
        self.form.label.setText(score)

    def startTimer(self, p_int, Qt_TimerType_timerType=None):
        p_int = 500



def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyStopWatch()
        window.show()
        sys.exit(app.exec_())

main()