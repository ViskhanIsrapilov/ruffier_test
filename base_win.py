"""Base window helpers used across the application."""

from PyQt5.QtWidgets import QWidget

from instr import win_height, win_width, win_x, win_y


# A small CSS snippet that is applied to all windows so the application
# looks a little more joyful and less like a plain Qt demo.  The colours
# were chosen to be bright but still readable.
APP_STYLE = """
QWidget {
    background-color: #fff5f5;
    font-size: 16px;
}
QLabel {
    color: #444;
}
QLineEdit {
    border: 1px solid #ff9aae;
    border-radius: 6px;
    padding: 4px;
    background: #ffffff;
}
QPushButton {
    background-color: #ff9aae;
    color: white;
    border-radius: 8px;
    padding: 6px 12px;
}
QPushButton:hover {
    background-color: #ff6085;
}
"""


class BaseWin(QWidget):
    """Common window setup utilities."""

    def set_appear(self, title: str) -> None:
        """Configure standard window geometry, title and style."""
        self.setWindowTitle(title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        # Apply the global style so each window uses the same colourful theme.
        self.setStyleSheet(APP_STYLE)
