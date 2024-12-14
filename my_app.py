from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        ''' The window where the greeting is located in '''
        super().__init__()
        # Creating and configuring graphic elements
        self.initUI()
        # Establishing connections between elements
        self.connects()
        # Sets what the window will look like [label, size, location]
        self.set_appear()
        # Start
        self.show()

    def initUI(self):
        ''' Creates graphic elements '''
        self.btn_next = QPushButton(text_next, self)
        self.lbl_hello = QLabel(txt_hello)
        self.lbl_instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.lbl_hello, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.lbl_instruction, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        ''' Sets what the window will look like [label, size, location] '''
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
