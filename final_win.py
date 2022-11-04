from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget

class FinalWin(QWidget):
  def __init__(self, exp):
    super().__init__()
    self.set_appear()
    self.exp = exp
    self.initUI()
    self.show()
    self.index = 0

  def set_appear(self):
    self.setWindowTitle('Результаты')
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def  initUI(self):
    self.v_line = QVBoxLayout()
    
    self.heart_text = QLabel(txt_workheart + self.results())
    
    self.index_text = QLabel(txt_index + str(self.index))


    self.v_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
    self.v_line.addWidget(self.heart_text, alignment = Qt.AlignCenter)
    self.setLayout(self.v_line)

  def results(self):
    if self.exp.age < 7:
      self.index = 0
      return 'результаты по этому возрасту отсутсвуют'
    self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
    if self.exp.age >= 15:
      if self.index >= 15:
        return txt_res1
      elif self.index < 15 and self.index >= 11:
        return txt_res2
      elif self.index < 11 and self.index >= 6:
        return txt_res3
      elif self.index < 6 and self.index >= 0.5:
        return txt_res4
      else: 
        return txt_res5
    if self.exp.age < 14 and self.exp.age >= 13:
      if self.index >= 16.5:
        return txt_res1
      elif self.index < 16.5 and self.index >= 12.5:
        return txt_res2
      elif self.index < 12.5 and self.index >= 7.5:
        return txt_res3
      elif self.index < 7.5 and self.index >= 2:
        return txt_res4
      else: 
        return txt_res5
    if self.exp.age < 12 and self.exp.age >= 11:
      if self.index >= 18:
        return txt_res1
      elif self.index < 18 and self.index >= 14:
        return txt_res2
      elif self.index < 14 and self.index >= 9:
        return txt_res3
      elif self.index < 9 and self.index >= 3.5:
        return txt_res4
      else: 
        return txt_res5
    if self.exp.age < 10 and self.exp.age >= 9:
      if self.index >= 19.5:
        return txt_res1
      elif self.index < 19.5 and self.index >= 15.5:
        return txt_res2
      elif self.index < 15.5 and self.index >= 10.5:
        return txt_res3
      elif self.index < 10.5 and self.index >= 5:
        return txt_res4
      else: 
        return txt_res5
    if self.exp.age < 8 and self.exp.age >= 7:
      if self.index >= 21:
        return txt_res1
      elif self.index < 21 and self.index >= 17:
        return txt_res2
      elif self.index < 17 and self.index >= 12:
        return txt_res3
      elif self.index < 12 and self.index >= 6.5:
        return txt_res4
      else: 
        return txt_res5