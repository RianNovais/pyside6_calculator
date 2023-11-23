from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE
from utils import isEmpty

# Display class, which will show the numbers clicked or typed

class Display(QLineEdit):
    enterPressed = Signal()
    backspacePressed = Signal()
    escPressed = Signal()

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE*2)
        self.setFocus()

        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.setTextMargins(BIG_FONT_SIZE, BIG_FONT_SIZE, BIG_FONT_SIZE, BIG_FONT_SIZE)

        self.setMinimumWidth(500)

    def keyPressEvent(self, event:QKeyEvent):
        key = event.key()
        KEYS = Qt.Key
        textNormal = event.text()
        text = textNormal.strip()

        if key == KEYS.Key_Enter or key == KEYS.Key_Return:
            self.enterPressed.emit()
            return event.ignore()

        if key == KEYS.Key_Backspace or key == KEYS.Key_Delete:
            self.backspacePressed.emit()
            return event.ignore()

        if key == KEYS.Key_Escape:
            self.escPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()