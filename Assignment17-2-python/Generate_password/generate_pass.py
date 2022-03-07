import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class GeneratePassword(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.setWindowTitle('Generate Password')
        self.ui = loader.load('form.ui',None)
        self.ui.show()

        self.list_choice = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','u','x','y','z',
                            '@','#','$','%','&','*','1','2','3','4','5','6','7','8','9']

        self.ui.btn_pass.clicked.connect(self.generate)
        self.flag_empty = True

        self.ui.rb_8.setChecked(True)
        

    def generate(self):
        if self.ui.rb_8.isChecked():
            self.string = ''
            list_of_random_items = random.sample(self.list_choice, 8)
            for i in range(len(list_of_random_items)):
                self.string += list_of_random_items[i]
            self.ui.lineEdit.setText(self.string)

        elif self.ui.rb_12.isChecked():
            self.string = ''
            list_of_random_items = random.sample(self.list_choice, 12)
            for i in range(len(list_of_random_items)):
                self.string += list_of_random_items[i]
            self.ui.lineEdit.setText(self.string)
        
        elif self.ui.rb_20.isChecked():
            self.string = ''
            list_of_random_items = random.sample(self.list_choice, 20)
            for i in range(len(list_of_random_items)):
                self.string += list_of_random_items[i]
            self.ui.lineEdit.setText(self.string)
        
                
        
app = QApplication([])

window = GeneratePassword()

app.exec()
