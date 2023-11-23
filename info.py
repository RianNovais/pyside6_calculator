from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import MEDIUM_FONT_SIZE

# information class, which will be a label and will be on top of the display, will show the result
class Info(QLabel):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size:{MEDIUM_FONT_SIZE}px')