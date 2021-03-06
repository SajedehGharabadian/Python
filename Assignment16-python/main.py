from functools import partial
import math

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Hello_World(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()

        self.ui.btn_start.clicked.connect(self.start)

        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_mod.clicked.connect(self.mod)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_pn.clicked.connect(self.num_pn)
        self.ui.btn_po.clicked.connect(self.num_po)


        self.ui.btn_0.clicked.connect(partial(self.function_num,0))
        self.ui.btn_1.clicked.connect(partial(self.function_num,1))
        self.ui.btn_2.clicked.connect(partial(self.function_num,2))
        self.ui.btn_3.clicked.connect(partial(self.function_num,3))
        self.ui.btn_4.clicked.connect(partial(self.function_num,4))
        self.ui.btn_5.clicked.connect(partial(self.function_num,5))
        self.ui.btn_6.clicked.connect(partial(self.function_num,6))
        self.ui.btn_7.clicked.connect(partial(self.function_num,7))
        self.ui.btn_8.clicked.connect(partial(self.function_num,8))
        self.ui.btn_9.clicked.connect(partial(self.function_num,9))
        
        self.flag_sum = 0
        self.flag_sub = 0
        self.flag_mul = 0
        self.flag_div = 0
        self.flag_mod = 0
        self.flag_point = 0


    def start(self):
        self.ui.textbox.setText('')

    def function_num(self,x):
        self.ui.textbox.setText(self.ui.textbox.text()+str(x))
        self.num2 = float(self.ui.textbox.text())
        

    def sum(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_sum = 1

    def sub(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_sub = 1

    def mul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_mul = 1

    def div(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_div = 1

    def mod(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_mod = 1

    def sin(self):
        self.num1 = float(self.ui.textbox.text())
        self.result = math.sin(math.radians(self.num1))
        self.ui.textbox.setText(str(self.result))

    def cos(self):
        self.num1 = float(self.ui.textbox.text())
        self.result = math.cos(math.radians(self.num1))
        self.ui.textbox.setText(str(self.result))

    def tan(self):
        self.num1 = float(self.ui.textbox.text())
        self.result = math.tan(math.radians(self.num1))
        self.ui.textbox.setText(str(self.result))

    def cot(self):
        self.num1 = float(self.ui.textbox.text())
        sin_num = math.sin(math.radians(self.num1))
        cos_num = math.cos(math.radians(self.num1))
        self.result = cos_num / sin_num
        self.ui.textbox.setText(str(self.result))

    def log(self):
        self.num1 = float(self.ui.textbox.text())
        self.result = math.log(self.num1)
        self.ui.textbox.setText(str(self.result))

    def sqrt(self):
        self.num1 = float(self.ui.textbox.text())
        self.result = math.sqrt(self.num1)
        self.ui.textbox.setText(str(self.result))

    def num_pn(self):
        self.ui.textbox.setText(str(float(self.ui.textbox.text()) * (-1)))

    def num_po(self):
        self.num = self.ui.textbox.text()
        count = self.num.count('.')
        if count == 0:
            self.ui.textbox.setText(self.ui.textbox.text()+'.')

    def equal(self):
        if self.flag_sum == 1:
            self.result = self.num1 + self.num2 
            self.flag_sum = 0
            #print(self.result)

        elif self.flag_sub == 1:
            self.result = self.num1 - self.num2 
            self.flag_sub = 0
            #print(self.result)

        elif self.flag_mul == 1:
            self.result = self.num1 * self.num2
            self.flag_mul = 0
            #print(self.result)

        elif self.flag_div == 1:
            try:
                self.result = self.num1 / self.num2
                self.flag_div = 0
            except ZeroDivisionError:
                return self.ui.textbox.setText('Error')
                #self.ui.textbox.setText('')

        elif self.flag_mod == 1:
            self.result = self.num1 % self.num2
            self.flag_mod = 0
            


        self.ui.textbox.setText(str(self.result))


app = QApplication([])

window = Hello_World()

app.exec()



