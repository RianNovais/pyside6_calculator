from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE
from utils import isEmpty

# Display class, which will show the numbers clicked or typed

class Display(QLineEdit):
    #signals of key
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

    #here we capture the button click events that take numbers and letters to the display (QLineEdit) and block the user
    # from typing. and here we handle some values that the user can type via the keyboard, such as the "Enter", "Esc"
    # and BACKSPACE keys, enter performs the operation, esc clears the screen, and backspace clears the last character
    # from the display, here we emit a .emit for the respective signals, which will be passed to the button class,
    # where we will connect these signals to the respective slots
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