from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget
from second_win import *

class MainWin(QWidget):
    def __init__(self):

        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):

        self.setWindowTitle('Тест Руфье')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):

        #направляющие
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        #привязка
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    

    def connects(self):
        
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        
        self.hide()
        self.tw = TestWin()


app = QApplication([])
mw = MainWin()
app.exec_()
