
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.setWindowTitle('Generate Password')
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.load_data()
        self.ui.rb_pr_to_en.setChecked(True)
        self.ui.btn_translate.clicked.connect(self.translate)
        self.ui.btn_clear.clicked.connect(self.clear)
    
    def load_data(self):
        self.mywords = []
        f = open('translate.txt' , 'r',encoding='utf8')
        rows = f.read().split('\n')

        for i in range(0,len(rows) , 2):
            En_word = rows[i]
            Pr_word = rows[i+1]
            self.mywords.append({'english' : En_word , 'persian' : Pr_word })

        print(self.mywords)


    def translate(self):
        if self.ui.rb_pr_to_en.isChecked():
            self.persian_to_english()

        elif self.ui.rb_en_to_pr.isChecked():
            self.english_to_persian()

        
    
    def persian_to_english(self):
        self.ui.lineEdit.setText('')
        self.text = self.ui.lineEdit_2.text()
        self.words = self.text.split(' ')
        for i in range(len(self.words)):
            for j in range(len(self.mywords)):
                if self.words[i] == self.mywords[j]['persian']:
                    self.word_pr = self.mywords[j]['english']
                    self.ui.lineEdit.setText(self.word_pr + ' ' + self.ui.lineEdit.text())


    def english_to_persian(self):
        self.ui.lineEdit_2.setText('')
        self.text = self.ui.lineEdit.text().lower()
        self.words = self.text.split(' ')
        for i in range(len(self.words)):
            for j in range(len(self.mywords)):
                if self.words[i] == self.mywords[j]['english']:
                    self.word_pr = self.mywords[j]['persian']
                    self.ui.lineEdit_2.setText(self.word_pr + ' ' + self.ui.lineEdit_2.text())
      

    def clear(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')


app = QApplication([])

window = Translator()

app.exec()
