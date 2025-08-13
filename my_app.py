from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import *
from base_win import BaseWin


class MainWin(BaseWin):
    def __init__(self):
        super().__init__()
        self.set_appear(txt_title)
        self.iniUI()
        self.connects()
        self.show()

    def iniUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
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

