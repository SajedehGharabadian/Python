import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class GuessNumber(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.setWindowTitle('Guess Number')
        self.ui = loader.load('form_guessnumber.ui',None)
        self.ui.show()
        self.ui.rb_1.setChecked(True)

        self.ui.btn_new_game.clicked.connect(self.new_game)
        self.ui.btn_res.clicked.connect(self.check)
        self.generate_num()

    def generate_num(self):
        if self.ui.rb_1.isChecked():
            self.random_num = random.randint(0,100)
            
        elif self.ui.rb_2.isChecked():
            self.random_num = random.randint(100,500)
            

    def check(self):
        self.num = int(self.ui.textbox.text())

        if self.num > self.random_num :
            msg_box = QMessageBox()
            msg_box.setText('your number is greater than random number!')
            msg_box.exec()
            self.ui.textbox.setText('')


        elif self.num < self.random_num:
            msg_box = QMessageBox()
            msg_box.setText('your number is smaller than random number!')
            msg_box.exec()
            self.ui.textbox.setText('')

        elif self.num == self.random_num:
            msg_box = QMessageBox()
            msg_box.setText('You win')
            msg_box.exec()
            self.ui.textbox.setText('')


    def new_game(self):
        self.generate_num()
        self.ui.textbox.setText('')
        



app = QApplication([])

window = GuessNumber()

app.exec()
