from functools import partial
import random 

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()

        self.game = [[self.ui.btn_1,self.ui.btn_2,self.ui.btn_3],
                     [self.ui.btn_4,self.ui.btn_5,self.ui.btn_6],
                     [self.ui.btn_7,self.ui.btn_8,self.ui.btn_9]]
        
        self.ui.btn_start.clicked.connect(self.new_game)
        self.ui.btn_help.clicked.connect(self.help)

        self.counter = 0
        self.cnt_com = 0
        self.cnt_win_x = 0
        self.cnt_win_o = 0
        self.cnt_equal = 0
        self.flag_play = True
        
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color:skyblue')
                self.game[i][j].clicked.connect(partial(self.play,i,j))

            
    def play(self,i,j):
        if self.flag_play:
            if self.ui.rb_player.isChecked() and self.game[i][j].text() == '':
              self.player(i,j)


            elif self.ui.rb_com.isChecked() and self.game[i][j].text() == '':
                self.play_com(i,j)


    def player(self,i,j):
        if self.counter % 2 == 0:
            self.game[i][j].setText('X')
            self.game[i][j].setStyleSheet('color:green; background-color:skyblue')
            self.counter += 1
                    
                
        elif self.counter % 2 == 1:
            self.game[i][j].setText('O')
            self.game[i][j].setStyleSheet('color:yellow; background-color:skyblue')
            self.counter += 1

        self.check()
        self.equal(self.counter)

    def play_com(self,i,j):
        self.player(i,j)
       
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if self.game[row][col].text() == '':
                break
           
        self.player(row,col)        

    def check(self):
        #satri 
        j=0
        for i in range (3):
            if self.game[i][j].text() == self.game[i][j+1].text() == self.game[i][j+2].text() == 'X':
                #self.flag_win_x = 1
                self.cnt_win_x += 1
                msg_box = QMessageBox()
                msg_box.setText('Player X wins')
                msg_box.exec()
                self.ui.lb_win_x.setText('X '+'\t'+str(self.cnt_win_x))
                self.flag_play = False
                self.refresh_game()
            
            elif self.game[i][j].text() == self.game[i][j+1].text() == self.game[i][j+2].text() == 'O':
                self.cnt_win_o += 1
                msg_box = QMessageBox()
                msg_box.setText('Player O wins')
                msg_box.exec()
                self.ui.lb_win_o.setText('O '+'\t'+str(self.cnt_win_o))
                self.flag_play = False
                self.refresh_game()   
        
        #sotoni
        i=0
        for j in range(3):
            if self.game[i][j].text() == self.game[i+1][j].text() == self.game[i+2][j].text() == 'X':
                self.cnt_win_x += 1
                msg_box = QMessageBox()
                msg_box.setText('Player X wins')
                msg_box.exec()
                self.ui.lb_win_x.setText('X '+'\t'+str(self.cnt_win_x))
                self.flag_play = False
                self.refresh_game()
                
                    
            elif self.game[i][j].text() == self.game[i+1][j].text() == self.game[i+2][j].text() == 'O' :
                self.cnt_win_o += 1
                msg_box = QMessageBox()
                msg_box.setText('Player O wins')
                msg_box.exec()
                self.ui.lb_win_o.setText('O '+'\t'+str(self.cnt_win_o))
                self.flag_play = False
                self.refresh_game()
               
               
        # ghotr asli
        k=0
        if self.game[k][k].text() == self.game[k+1][k+1].text() == self.game[k+2][k+2].text() == 'X':
           self.cnt_win_x += 1
           msg_box = QMessageBox()
           msg_box.setText('Player X wins')
           msg_box.exec()
           self.ui.lb_win_x.setText('X '+'\t'+str(self.cnt_win_x))
           self.flag_play = False
           self.refresh_game()

        elif self.game[k][k].text() == self.game[k+1][k+1].text() == self.game[k+2][k+2].text() == 'O':
            self.cnt_win_o += 1
            msg_box = QMessageBox()
            msg_box.setText('Player O wins')
            msg_box.exec()
            self.ui.lb_win_o.setText('O '+'\t'+str(self.cnt_win_o))
            self.flag_play = False
            self.refresh_game()
               
        
        #ghotr faree
        j=2
        i=0
        if self.game[i][j].text() == self.game[i+1][j-1].text() == self.game[i+2][j-2].text() == 'X':
            self.cnt_win_x += 1
            msg_box = QMessageBox()
            msg_box.setText('Player X wins')
            msg_box.exec()
            self.ui.lb_win_x.setText('X '+'\t'+str(self.cnt_win_x))
            self.flag_play = False
            self.refresh_game()
            
        elif self.game[i][j].text() == self.game[i+1][j-1].text() == self.game[i+2][j-2].text() == 'O':
            self.cnt_win_o += 1
            msg_box = QMessageBox()
            msg_box.setText('Player O wins')
            msg_box.exec()
            self.ui.lb_win_o.setText('O '+'\t'+str(self.cnt_win_o))
            self.flag_play = False
            self.refresh_game()
    
    def equal(self,cnt):
        if cnt == 9 and self.cnt_win_o == 0 and self.cnt_win_x == 0:
           msg_box = QMessageBox()
           msg_box.setText('No one win')
           msg_box.exec()
           self.flag_play = False
        


    def refresh_game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color:skyblue')

        self.counter = 0
        self.flag_play = True

    def new_game(self):
        self.refresh_game()
        
    
    def help(self):
        msgbox = QMessageBox()
        msgbox.setText('XO game \nVersion 1.0')
        msgbox.exec()


app = QApplication([])

window = TicTacToe()

app.exec()

