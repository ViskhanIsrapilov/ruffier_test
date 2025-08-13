from PyQt5.QtWidgets import QWidget
from instr import win_width, win_height, win_x, win_y


class BaseWin(QWidget):
    """Common window setup utilities."""

    def set_appear(self, title: str) -> None:
        """Configure standard window geometry and title."""
        self.setWindowTitle(title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
