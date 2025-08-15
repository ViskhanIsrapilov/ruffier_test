from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)
from instr import *
from final_win import *
from base_win import BaseWin


class AutoSelectLineEdit(QLineEdit):
    """Line edit that selects its content on focus and jumps to the next widget on Enter."""

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.focusNextChild()
        else:
            super().keyPressEvent(event)


def make_icon(text: str, color: str = "#ff9aae") -> QLabel:
    """Create a simple square pixmap with centered text to act as an icon."""
    pix = QPixmap(24, 24)
    pix.fill(QColor(color))
    painter = QPainter(pix)
    painter.setPen(Qt.white)
    font = QFont()
    font.setBold(True)
    painter.setFont(font)
    painter.drawText(pix.rect(), Qt.AlignCenter, text)
    painter.end()
    lbl = QLabel()
    lbl.setPixmap(pix)
    return lbl


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
        self.name = AutoSelectLineEdit(txt_hintname)
        self.name.setStyleSheet("font-size: 16px;")
        self.name_icon = make_icon("N")

        self.txt_age = QLabel(txt_age)
        self.txt_age.setStyleSheet("font-size: 18px; color: #1e6091;")
        self.age = AutoSelectLineEdit(txt_hintage)
        self.age.setStyleSheet("font-size: 16px;")
        self.age_icon = make_icon("A")
        self.test1 = QLabel(txt_test1)
        self.test1.setWordWrap(True)
        self.test1.setStyleSheet("font-size: 14px; color: #444;")
        self.button_test1 = QPushButton(txt_starttest1)
        self.button_test1.setStyleSheet("font-size: 16px;")
        self.result_test1 = AutoSelectLineEdit(txt_hinttest1)
        self.result_test1.setStyleSheet("font-size: 16px;")
        self.result_test1_icon = make_icon("1")
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
        self.test_result_first = AutoSelectLineEdit(txt_hinttest2)
        self.test_result_first.setStyleSheet("font-size: 16px;")
        self.test_result_first_icon = make_icon("2")
        self.test_result_end = AutoSelectLineEdit(txt_hinttest3)
        self.test_result_end.setStyleSheet("font-size: 16px;")
        self.test_result_end_icon = make_icon("3")
        self.button_send_results = QPushButton(txt_sendresults)
        self.button_send_results.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )

        self.layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_icon)
        name_layout.addWidget(self.name)
        name_layout.setAlignment(Qt.AlignCenter)

        age_layout = QHBoxLayout()
        age_layout.addWidget(self.age_icon)
        age_layout.addWidget(self.age)
        age_layout.setAlignment(Qt.AlignCenter)

        res1_layout = QHBoxLayout()
        res1_layout.addWidget(self.result_test1_icon)
        res1_layout.addWidget(self.result_test1)
        res1_layout.setAlignment(Qt.AlignCenter)

        res2_layout = QHBoxLayout()
        res2_layout.addWidget(self.test_result_first_icon)
        res2_layout.addWidget(self.test_result_first)
        res2_layout.setAlignment(Qt.AlignCenter)

        res3_layout = QHBoxLayout()
        res3_layout.addWidget(self.test_result_end_icon)
        res3_layout.addWidget(self.test_result_end)
        res3_layout.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.txt_name, alignment=Qt.AlignCenter)
        self.layout.addLayout(name_layout)
        self.layout.addWidget(self.txt_age)
        self.layout.addLayout(age_layout)
        self.layout.addWidget(self.test1)
        self.layout.addWidget(self.button_test1)
        self.layout.addLayout(res1_layout)
        self.layout.addWidget(self.test2)
        self.layout.addWidget(self.button_test2)
        self.layout.addWidget(self.test3)
        self.layout.addWidget(self.button_test3)
        self.layout.addLayout(res2_layout)
        self.layout.addLayout(res3_layout)
        self.layout.addWidget(self.button_send_results, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button_send_results.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

