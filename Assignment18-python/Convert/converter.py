from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Convert(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.setWindowTitle('convert')
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.ui.cmbox_1.addItems(['mass','length','tempreture','digital volume'])
        self.ui.cmbox_1.activated.connect(self.check_index)
        #self.ui.btn_cal.clicked.connect(self.result)
        self.flag_mass_g_k = 0
        self.ui.textbox_in.returnPressed.connect(self.check_index)
        


    def check_index(self):
        ctext = self.ui.cmbox_1.currentText()
        if ctext == 'mass':
           self.ui.cmbox_from.addItems(['grams','kilograms','ton','pound'])
           self.ui.cmbox_to.addItems(['grams','kilograms','ton','pound'])
           self.ui.btn_cal.clicked.connect(self.check_mass)  

        elif ctext == 'length':
           self.ui.cmbox_from.addItems(['millimeters','centimeters','meters','kilometers','inches'])
           self.ui.cmbox_to.addItems(['millimeters','centimeters','meters','kilometers','inches'])
           self.ui.btn_cal.clicked.connect(self.check_length)  

        elif ctext == 'tempreture':
           self.ui.cmbox_from.addItems(['celsius','fahrenheit','kelvin'])
           self.ui.cmbox_to.addItems(['celsius','fahrenheit','kelvin'])
           self.ui.btn_cal.clicked.connect(self.check_tempreture)  

        
        elif ctext == 'digital volume':
           self.ui.cmbox_from.addItems(['bits','bytes','kilobytes','megabytes','gigabytes','terabytes'])
           self.ui.cmbox_to.addItems(['bits','bytes','kilobytes','megabytes','gigabytes','terabytes'])
           self.ui.btn_cal.clicked.connect(self.check_digital)  

    def check_mass(self):
        mtext1 = self.ui.cmbox_from.currentText()
        mtext2 = self.ui.cmbox_to.currentText()
        num = float(self.ui.textbox_in.text())

        if mtext1 == 'grams':
            if mtext2 == 'grams':
                self.result = num
                

            elif mtext2 == 'kilograms':
                self.result = num / 1000
                

            elif mtext2 == 'ton':
                self.result = num / 1000000
                

            elif mtext2 == 'pound':
                self.result = num * 0.0022
                

        elif mtext1 == 'kilograms':
            if mtext2 == 'grams':
                self.result = num * 1000 
               
            elif mtext2 == 'kilograms':
                self.result = num 
                
            elif mtext2 == 'ton':
                self.result = num / 1000
                self.ui.textbox_out.setText(str(self.result))
            
            elif mtext2 == 'pound':
                self.result = num * 2.205

        elif mtext1 == 'ton':
            if mtext2 == 'grams':
                self.result = num * 1000000 

            elif mtext2 == 'kilograms':
                self.result = num * 1000
            
            elif mtext2 == 'ton':
                self.result = num 
            
            elif mtext2 == 'pound':
                self.result = num * 2679.2289
                
        elif mtext1 == 'pound':
            if mtext2 == 'grams':
                self.result = num * 453.59237

            elif mtext2 == 'kilograms':
                self.result = num * 0.45359237

            elif mtext2 == 'ton':
                self.result = num * 0.0004535924
            
            elif mtext2 == 'pound':
                self.result = num
                

        self.ui.textbox_out.setText(str(self.result))

        
    def check_length(self):
        mtext1 = self.ui.cmbox_from.currentText()
        mtext2 = self.ui.cmbox_to.currentText()
        num = float(self.ui.textbox_in.text())

        if mtext1 == 'millimeters':
            if mtext2 == 'millimeters':
                self.result = num

            elif mtext2 == 'centimeters':
                self.result = num / 10

            elif mtext2 == 'meters':
                self.result = num / 1000

            elif mtext2 == 'kilometers':
                self.result = num / 1000000

            elif mtext2 == 'inches':
                self.result = num * 0.0394

        elif mtext1 == 'centimeters':
            if mtext2 == 'millimeters':
                self.result = num * 10

            elif mtext2 == 'centimeters':
                self.result = num 

            elif mtext2 == 'meters':
                self.result = num / 100

            elif mtext2 == 'kilometers':
                self.result = num / 100000

            elif mtext2 == 'inches':
                self.result = num * 0.3937

        elif mtext1 == 'meters':
            if mtext2 == 'millimeters':
                self.result = num * 1000

            elif mtext2 == 'centimeters':
                self.result = num * 100

            elif mtext2 == 'meters':
                self.result = num

            elif mtext2 == 'kilometers':
                self.result = num / 1000

            elif mtext2 == 'inches':
                self.result = num * 39.3700787

        elif mtext1 == 'kilometers':
            if mtext2 == 'millimeters':
                self.result = num * 1000000

            elif mtext2 == 'centimeters':
                self.result = num * 100000

            elif mtext2 == 'meters':
                self.result = num * 1000

            elif mtext2 == 'kilometers':
                self.result = num

            elif mtext2 == 'inches':
                self.result = num * 39370.0787

        elif mtext1 == 'inches':
            if mtext2 == 'millimeters':
                self.result = num * 1000000

            elif mtext2 == 'centimeters':
                self.result = num * 100000

            elif mtext2 == 'meters':
                self.result = num * 1000

            elif mtext2 == 'kilometers':
                self.result = num

            elif mtext2 == 'inches':
                self.result = num * 39370.0787
        
        self.ui.textbox_out.setText(str(self.result))


    def check_tempreture(self):
        mtext1 = self.ui.cmbox_from.currentText()
        mtext2 = self.ui.cmbox_to.currentText()
        num = float(self.ui.textbox_in.text())

        if mtext1 == 'celsius':
            if mtext2 == 'celsius':
                self.result = num  

            elif mtext2 == 'fahrenheit':
                self.result = (num * 9)/5 + 32

            elif mtext2 == 'kelvin':
                self.result = num + 273

        elif mtext1 == 'fahrenheit':
            if mtext2 == 'celsius':
                self.result = 5/9 * (num - 32)

            elif mtext2 == 'fahrenheit':
                self.result = num

            elif mtext2 == 'kelvin':
                temp = 5/9 * (num - 32)
                self.result = temp + 273

        elif mtext1 == 'kelvin':
            if mtext2 == 'celsius':
                self.result = num - 273

            elif mtext2 == 'fahrenheit':
                self.result = 1.8 * (num - 273) + 32

            elif mtext2 == 'kelvin':
                self.result = num

        self.ui.textbox_out.setText(str(self.result))


    def check_digital(self):
        mtext1 = self.ui.cmbox_from.currentText()
        mtext2 = self.ui.cmbox_to.currentText()
        num = float(self.ui.textbox_in.text())

        if mtext1 == 'bits':
            if mtext2 == 'bits':
                self.result = num 
            
            elif mtext2 == 'bytes':
                self.result = num * 0.125
            
            elif mtext2 == 'kilobytes':
                self.result = num * (1/8) * 0.001
            
            elif mtext2 == 'megabytes':
                self.result = num * (1/8) * 10**-6

            elif mtext2 == 'gigabytes':
                self.result = num * (1/8) * 10**-9

            elif mtext2 == 'terabytes':
                self.result = num * (1/8) * 10**-12

        
        elif mtext1 == 'bytes':
            if mtext2 == 'bits':
                self.result = num * 8
            
            elif mtext2 == 'bytes':
                self.result = num 
            
            elif mtext2 == 'kilobytes':
                self.result = num / 1024
            
            elif mtext2 == 'megabytes':
                self.result = num / (1024 ** 2)

            elif mtext2 == 'gigabytes':
                self.result = num /(1024 ** 3)

            elif mtext2 == 'terabytes':
                self.result = num / (1024 ** 4)

        elif mtext1 == 'kilobytes':
            if mtext2 == 'bits':
                self.result = num * 8000
            
            elif mtext2 == 'bytes':
                self.result = num * 1000
            
            elif mtext2 == 'kilobytes':
                self.result = num 
            
            elif mtext2 == 'megabytes':
                self.result = num / 1000

            elif mtext2 == 'gigabytes':
                self.result = num * 10**(-6)

            elif mtext2 == 'terabytes':
                self.result = num * 10**(-9)

        elif mtext1 == 'megabytes':
            if mtext2 == 'bits':
                self.result = num * 8 * (1000 ** 2)
            
            elif mtext2 == 'bytes':
                self.result = num * (1024 ** 2)
            
            elif mtext2 == 'kilobytes':
                self.result = num * 1000
            
            elif mtext2 == 'megabytes':
                self.result = num 

            elif mtext2 == 'gigabytes':
                self.result = num / 1000

            elif mtext2 == 'terabytes':
                self.result = num / 10**(6)

        elif mtext1 == 'gigabytes':
            if mtext2 == 'bits':
                self.result = num * 8 * (1000 ** 3)
            
            elif mtext2 == 'bytes':
                self.result = num * (1024 ** 3)
            
            elif mtext2 == 'kilobytes':
                self.result = num  * (1000 ** 2)
            
            elif mtext2 == 'megabytes':
                self.result = num * 1000

            elif mtext2 == 'gigabytes':
                self.result = num 

            elif mtext2 == 'terabytes':
                self.result = num / 1000

        elif mtext1 == 'terabytes':
            if mtext2 == 'bits':
                self.result = num * 8 * (1000 ** 4)
            
            elif mtext2 == 'bytes':
                self.result = num * (1024 ** 4)
            
            elif mtext2 == 'kilobytes':
                self.result = num  * (1000 ** 3)
            
            elif mtext2 == 'megabytes':
                self.result = num * (1000 ** 2)

            elif mtext2 == 'gigabytes':
                self.result = num * 1000

            elif mtext2 == 'terabytes':
                self.result = num 

        
app = QApplication([])

window = Convert()

app.exec()
