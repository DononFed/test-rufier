from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget
from final_win import *
from PyQt5.QtGui import  QFont

class Experiment():
    def __init__(self, age, test1, test2, test3):
       self.age = int(age)
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3


class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()


        self.btnf = QPushButton('Начать первый тест', self)
        self.btns = QPushButton('Начать делать приседания', self)
        self.btnt = QPushButton('Начать финальный тест', self)
        self.btn_next = QPushButton('Отправить результаты', self)
        self.timer = QLabel()
        self.text_name = QLabel('Введите Ф.И.О:', self)
        self.text_age = QLabel('Полных лет:', self)
        self.text_ex1 = QLabel(txt_test1, self)
        self.text_ex2 = QLabel(txt_test2, self)
        self.text_exf =QLabel(txt_test3, self)
        self.line_name = QLineEdit('Ф.И.О')
        self.line_age = QLineEdit('0')
        self.line_ex1 = QLineEdit('0')
        self.line_ex2 = QLineEdit('0')
        self.line_exf1 = QLineEdit('0')
        self.line_exf2 = QLineEdit('0')
        self.text_timer = QLabel(text_timer1)

        #кнопки
        #btn1 =
        #timer =

        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_ex1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btnf, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_ex1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_ex2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btns, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_exf, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_exf1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_exf2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btnt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment= Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)  
    def timer3Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.btnf.clicked.connect(self.timer_test)
        self.btns.clicked.connect(self.timer_sits)
        self.btnt.clicked.connect(self.timer_final)
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.exp = Experiment(self.line_age.text(), self.line_ex1.text(), self.line_exf1.text(), self.line_exf2.text())
        self.hide()
        self.fw = FinalWin(self.exp)


#app = QApplication([])
#mw = TestWin()
#app.exec_()
