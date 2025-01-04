from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
from final_win import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.iniUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def iniUI(self):
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.left_layout = QVBoxLayout(self)
        self.left_layout.addWidget(self.txt_index, alignment = Qt.AlignCenter)
        self.left_layout.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.left_layout)



