from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.iniUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def iniUI(self):
        self.txt_name = QLabel(txt_name)
        self.name = QLineEdit(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.age = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.button_test1 = QPushButton(txt_starttest1)
        self.result_test1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.button_test2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.button_test3 = QPushButton(txt_starttest3)
        self.test_result_first = QLineEdit(txt_hinttest2)
        self.test_result_end = QLineEdit(txt_hinttest3)
        self.button_send_results = QPushButton(txt_sendresults)

        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.left_layout = QVBoxLayout(self)
        self.right_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.left_layout.addWidget(self.txt_name, alignment = Qt.AlignCenter)
        self.left_layout.addWidget(self.name, alignment = Qt.AlignCenter)
        self.left_layout.addWidget(self.txt_age)
        self.left_layout.addWidget(self.age)
        self.left_layout.addWidget(self.test1)
        self.left_layout.addWidget(self.button_test1)
        self.left_layout.addWidget(self.result_test1)
        self.left_layout.addWidget(self.test2)
        self.left_layout.addWidget(self.button_test2)
        self.left_layout.addWidget(self.test3)
        self.left_layout.addWidget(self.button_test3)
        self.left_layout.addWidget(self.test_result_first)
        self.left_layout.addWidget(self.test_result_end)
        self.left_layout.addWidget(self.button_send_results, alignment = Qt.AlignCenter)
        # self.left_layout.addWidget(self.horizontal_layout)
        # self.horizontal_layout.addWidget(self.left_layout, alignment = Qt.AlignHCenter)
        # self.horizontal_layout.addWidget(self.right_layout)
        # self.horizontal_layout.addWidget(self.left_layout, alignment = Qt.AlignCenter)
        # self.setLayout(self.right_layout)
        self.setLayout(self.left_layout)
    def connects(self):
        self.button_send_results.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

