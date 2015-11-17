__author__ = 'Sawl_Stone'
# -​*- coding: utf-8 -*​-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore
import sys
#from fs_hw import *

class MyCalc(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("MyTdForm.ui") # Form - класс окошка в дизайнере
        self.form = Form()
        self.form.setupUi(self) # связываем объект Form(окошко) с виджетами

        # QPush_Buttons with button func
        #self.form.Exit.clicked.connect(Qt.qApp.quit) # Button "Exit"
        self.form.time_date_now.clicked.connect(self.date_time)
        
		# Buttons func
        
    def date_time(self):
        #self.form.label.setText(import fs_hw)
        import fs_hw
        self.form.label_tdn.setText(fs_hw.main())


def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyCalc()
        window.show()
        sys.exit(app.exec_())
        

main()
