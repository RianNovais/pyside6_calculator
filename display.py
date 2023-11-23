from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE

# Display class, which will show the numbers clicked or typed

class Display(QLineEdit):

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE*2)

        self.setFocus()

        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.setTextMargins(BIG_FONT_SIZE, BIG_FONT_SIZE, BIG_FONT_SIZE, BIG_FONT_SIZE)

        self.setMinimumWidth(500)
