from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QLineEdit
from instr import *
from final_win import *
from base_win import BaseWin


class TestWin(BaseWin):
    def __init__(self):
        super().__init__()
        self.set_appear(txt_title)
        self.iniUI()
        self.connects()
        self.show()

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

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_name, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.name, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.txt_age)
        self.layout.addWidget(self.age)
        self.layout.addWidget(self.test1)
        self.layout.addWidget(self.button_test1)
        self.layout.addWidget(self.result_test1)
        self.layout.addWidget(self.test2)
        self.layout.addWidget(self.button_test2)
        self.layout.addWidget(self.test3)
        self.layout.addWidget(self.button_test3)
        self.layout.addWidget(self.test_result_first)
        self.layout.addWidget(self.test_result_end)
        self.layout.addWidget(self.button_send_results, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button_send_results.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

