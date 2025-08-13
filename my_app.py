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
        self.hello_text.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #0077b6;"
        )
        self.instruction = QLabel(txt_instruction)
        self.instruction.setWordWrap(True)
        self.instruction.setStyleSheet("font-size: 16px; color: #333333;")
        self.button = QPushButton(txt_next)
        self.button.setStyleSheet("font-size: 18px;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()

