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
        self.txt_name.setStyleSheet("font-size: 18px; color: #1e6091;")
        self.name = QLineEdit(txt_hintname)
        self.name.setStyleSheet("font-size: 16px;")
        self.txt_age = QLabel(txt_age)
        self.txt_age.setStyleSheet("font-size: 18px; color: #1e6091;")
        self.age = QLineEdit(txt_hintage)
        self.age.setStyleSheet("font-size: 16px;")
        self.test1 = QLabel(txt_test1)
        self.test1.setWordWrap(True)
        self.test1.setStyleSheet("font-size: 14px; color: #444;")
        self.button_test1 = QPushButton(txt_starttest1)
        self.button_test1.setStyleSheet("font-size: 16px;")
        self.result_test1 = QLineEdit(txt_hinttest1)
        self.result_test1.setStyleSheet("font-size: 16px;")
        self.test2 = QLabel(txt_test2)
        self.test2.setWordWrap(True)
        self.test2.setStyleSheet("font-size: 14px; color: #444;")
        self.button_test2 = QPushButton(txt_starttest2)
        self.button_test2.setStyleSheet("font-size: 16px;")
        self.test3 = QLabel(txt_test3)
        self.test3.setWordWrap(True)
        self.test3.setStyleSheet("font-size: 14px; color: #444;")
        self.button_test3 = QPushButton(txt_starttest3)
        self.button_test3.setStyleSheet("font-size: 16px;")
        self.test_result_first = QLineEdit(txt_hinttest2)
        self.test_result_first.setStyleSheet("font-size: 16px;")
        self.test_result_end = QLineEdit(txt_hinttest3)
        self.test_result_end.setStyleSheet("font-size: 16px;")
        self.button_send_results = QPushButton(txt_sendresults)
        self.button_send_results.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )

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

