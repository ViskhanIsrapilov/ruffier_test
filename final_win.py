from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from instr import *
from base_win import BaseWin


class FinalWin(BaseWin):
    def __init__(self):
        super().__init__()
        self.set_appear(txt_finalwin)
        self.iniUI()
        self.show()

    def iniUI(self):
        self.txt_index = QLabel(txt_index)
        # Make the result headline stand out.
        self.txt_index.setStyleSheet("font-size: 24px; color: #d6336c;")
        self.txt_workheart = QLabel(txt_workheart)
        self.txt_workheart.setStyleSheet("font-size: 20px; color: #1e81b0;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.txt_workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)



