__author__ = 'Sawl_Stone'
# -​*- coding: utf-8 -*​-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore
import sys
import math

class MyCalc(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("MyCalcForm.ui") # Form - класс окошка в дизайнере
        self.form = Form()
        self.form.setupUi(self) # связываем объект Form(окошко) с виджетами

        # QPush_Buttons with button func
        self.form.Exit.clicked.connect(Qt.qApp.quit) # Button "Exit"
        self.form.one_num.clicked.connect(self.one_num_button)
        self.form.two_num.clicked.connect(self.two_num_button)
        self.form.three_num.clicked.connect(self.three_num_button)
        self.form.four_num.clicked.connect(self.four_num_button)
        self.form.five_num.clicked.connect(self.five_num_button)
        self.form.six_num.clicked.connect(self.six_num_button)
        self.form.seven_num.clicked.connect(self.seven_num_button)
        self.form.eight_num.clicked.connect(self.eight_num_button)
        self.form.nine_num.clicked.connect(self.nine_num_button)
        self.form.zero_num.clicked.connect(self.zero_num_button)

        # QPush_Buttons with operation func
        self.form.plus.clicked.connect(self.plus_button)
        self.form.minus.clicked.connect(self.minus_button)
        self.form.multiply.clicked.connect(self.multiply_button)
        self.form.divide.clicked.connect(self.divide_button)
        self.form.equally.clicked.connect(self.equally_button)
        self.form.delete_all.clicked.connect(self.delete_all_button)
        #self.form.delete_2.clicked.connect(self.delete_2_button)
        #self.form.koma.clicked.connect(self.koma_button)
        self.form.sqrt.clicked.connect(self.sqrt_button)

        self.input_list_1 = 0
        self.input_list_2 = 0
        self.symbol_list = ""
        self.output_list = 0

        # Buttons func
        
    def one_num_button(self):
        one = self.form.label.text()
        if len(one) < 11:
            if one != '0':      self.form.label.setText(one + '1')
            else:               self.form.label.setText('1')

    def two_num_button(self):
        two = self.form.label.text()
        if len(two) < 11:
            if two != '0':      self.form.label.setText(two + '2')
            else:               self.form.label.setText('2')

    def three_num_button(self):
        three = self.form.label.text()
        if len(three) < 11:
            if three != '0':    self.form.label.setText(three + '3')
            else:               self.form.label.setText('3')

    def four_num_button(self):
        four = self.form.label.text()
        if len(four) < 11:
            if four != '0':     self.form.label.setText(four + '4')
            else:               self.form.label.setText('4')

    def five_num_button(self):
        five = self.form.label.text()
        if len(five) < 11:
            if five != '0':     self.form.label.setText(five + '5')
            else:               self.form.label.setText('5')

    def six_num_button(self):
        six = self.form.label.text()
        if len(six) < 11:
            if six != '0':      self.form.label.setText(six + '6')
            else:               self.form.label.setText('6')

    def seven_num_button(self):
        seven = self.form.label.text()
        if len(seven) < 11:
            if seven != '0':    self.form.label.setText(seven + '7')
            else:               self.form.label.setText('7')

    def eight_num_button(self):
        eight = self.form.label.text()
        if len(eight) < 11:
            if eight != '0':    self.form.label.setText(eight + '8')
            else:               self.form.label.setText('8')

    def nine_num_button(self):
        nine = self.form.label.text()
        if len(nine) < 11:
            if nine != '0':     self.form.label.setText(nine + '9')
            else:               self.form.label.setText('9')

    def zero_num_button(self):
        zero = self.form.label.text()
        if len(zero) < 11:
            if zero != '0':     self.form.label.setText(zero + '0')
            else:               self.form.label.setText('0')

        # Operation func
    def plus_button(self):
        self.input_list_1 = int(self.form.label.text())
        self.form.label.setText(None)
        self.form.label_2.setText(str(self.input_list_1) + ' +')
        self.sumbol_list = 'plus'

    def minus_button(self):
        self.input_list_1 = int(self.form.label.text())
        self.form.label.setText(None)
        self.form.label_2.setText(str(self.input_list_1) + ' -')
        self.sumbol_list = 'minus'

    def multiply_button(self):
        self.input_list_1 = int(self.form.label.text())
        self.form.label.setText(None)
        self.form.label_2.setText(str(self.input_list_1) + ' *')
        self.sumbol_list = 'multiply'

    def divide_button(self):
        self.input_list_1 = int(self.form.label.text())
        self.form.label.setText(None)
        self.form.label_2.setText(str(self.input_list_1) + ' /')
        self.sumbol_list = 'divide'

    def sqrt_button(self):
        self.input_list_1 = int(self.form.label.text())
        self.form.label_2.setText(str(self.input_list_1) + ' sqrt')
        self.sumbol_list = 'sqrt'

    def delete_all_button(self):
        self.form.label.setText('0')
        #self.form.label_2.setText(None)
        self.input_list_1 = 0
        self.input_list_2 = 0
        self.symbol_list = ""
        self.output_list = 0

    def equally_button(self):
        self.input_list_2 = int(self.form.label.text())
        if self.sumbol_list == 'plus':
            self.output_list = int(self.input_list_1) + int(self.input_list_2)
            self.form.label_2.setText(str(self.input_list_1) + ' + ' + str(self.input_list_2) + ' =')
            #self.form.label.setText(str(self.output_list))
        elif self.sumbol_list == 'minus':
            self.output_list = int(self.input_list_1) - int(self.input_list_2)
            self.form.label_2.setText(str(self.input_list_1) + ' - ' + str(self.input_list_2) + ' =')
            #self.form.label.setText(str(self.output_list))
        elif self.sumbol_list == 'multiply':
            self.output_list = int(self.input_list_1) * int(self.input_list_2)
            self.form.label_2.setText(str(self.input_list_1) + ' * ' + str(self.input_list_2) + ' =')
            #self.form.label.setText(str(self.output_list))
        elif self.sumbol_list == 'divide':
            self.output_list = int(self.input_list_1) / int(self.input_list_2)
            self.form.label_2.setText(str(self.input_list_1) + ' / ' + str(self.input_list_2) + ' =')
        self.form.label.setText(str(self.output_list))

def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyCalc()
        window.show()
        sys.exit(app.exec_())
        

main()
