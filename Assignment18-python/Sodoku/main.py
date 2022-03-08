import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6 import QtCore

class Soduko(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.setWindowTitle('Sodoku')
        self.ui = loader.load('form.ui',None)

        self.game = [[None for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 32px')
                tb.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
                self.game[i][j] = tb
                self.game[i][j].textChanged.connect(self.checkGame)
                self.ui.mygrid.addWidget(tb,i,j)

        self.ui.show()
        self.ui.btn_newgame.clicked.connect(self.new_Game)
        self.ui.btn_check.clicked.connect(self.checkGame)
        self.ui.btn_reset.clicked.connect(self.reset_Game)
        self.ui.btn_mode.clicked.connect(self.Dark_Mode)
        self.flag_for_dark_mode = False

    def Dark_Mode(self):
        if self.ui.btn_mode.text() == 'Dark Mode':
            self.ui.setStyleSheet('color: white; background-color: gray')
            for i in range(9):
                for j in range(9):
                    self.game[i][j].setStyleSheet('font-size: 32px ; color :black;background-color:gray')

            self.ui.btn_reset.setStyleSheet('font-size: 11px;background-color:gray;color:white')
            self.ui.btn_newgame.setStyleSheet('font-size: 11px;background-color:gray;color:white')
            self.ui.btn_check.setStyleSheet('font-size: 11px;background-color:gray;color:white')
            self.ui.btn_mode.setStyleSheet('font-size: 11px;background-color:gray;color:white')
            self.ui.btn_mode.setText('Light Mode')
            self.flag_for_dark_mode = True
            
        elif self.ui.btn_mode.text() == 'Light Mode':
            for i in range(9):
                for j in range(9):
                    self.game[i][j].setStyleSheet('font-size: 32px ; color : black;background-color:white')

            self.ui.btn_reset.setStyleSheet('font-size: 11px;background-color:white;color:black')
            self.ui.btn_newgame.setStyleSheet('font-size: 11px;background-color:white;color:black')
            self.ui.btn_check.setStyleSheet('font-size: 11px;background-color:white;color:black')
            self.ui.btn_mode.setStyleSheet('font-size: 11px;background-color:white;color:black')
            self.ui.btn_mode.setText('Dark Mode')
            self.flag_for_dark_mode = True
            


    def checkGame(self):
        self.flag_win = True
        #check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size: 32px;color:black;background-color:pink')
                        self.flag_win = False
                        

        #check columns
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size: 32px;color:black;background-color:pink')
                        self.flag_win = False
                        
        #check 3x3                

        for row in range(3):
            for col in range(3):
                for i in range(3):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and row != i and col != j and self.game[row][col].text() != '':
                            self.game[row][col].setStyleSheet('font-size: 32px;color:black;background-color:pink')
                            self.flag_win = False
                            

        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    self.flag_win = False
                    break

        if self.flag_win:       
            msg_box = QMessageBox()
            msg_box.setText('Congratulation')
            msg_box.exec()

    def reset_Game(self):
    
        file_path = f"data/s{self.r}.txt"
        f = open(file_path,'r')
        big_text = f.read()
        rows = big_text.split('\n')

        for i in range(len(rows)):
            numbers = rows[i].split(' ')
            for j in range(9):
                if numbers[j]  == '0':
                    self.game[i][j].setText('')
                    self.game[i][j].setStyleSheet('font-size: 32px;color:black')
                    self.game[i][j].setAlignment(QtCore.Qt.AlignCenter) 
                    self.game[i][j].setReadOnly(False)
                else:
                    self.game[i][j].setText(numbers[j])
                    self.game[i][j].setAlignment(QtCore.Qt.AlignCenter)
                    self.game[i][j].setReadOnly(True) 

        

    def new_Game(self):
        try:
            for i in range(9):
                for j in range(9):
                    self.game[i][j].setText('') 

            self.r = random.randint(1,6)
            file_path = f"data/s{self.r}.txt"
            f = open(file_path,'r')
            big_text = f.read()
            rows = big_text.split('\n')

            for i in range(len(rows)):
                numbers = rows[i].split(' ')
                for j in range(9):
                    if numbers[j]  == '0':
                        self.game[i][j].setText('')
                        self.game[i][j].setStyleSheet('font-size: 32px;color:black')
                        self.game[i][j].setAlignment(QtCore.Qt.AlignCenter)
                        self.game[i][j].setReadOnly(False)
                    else:
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setAlignment(QtCore.Qt.AlignCenter)
                        self.game[i][j].setReadOnly(True)
                    

        except:
            msg_box = QMessageBox()
            msg_box.setText('You can not load this file')
            msg_box.exec()

                        

app = QApplication([])

window = Soduko()

app.exec()
