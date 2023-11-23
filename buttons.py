from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QGridLayout
from variables import MEDIUM_FONT_SIZE
from typing import TYPE_CHECKING
from display import Display
from info import Info
from utils import isNumOrDot, isEmpty, isValidNumber

# to avoid circular import
if TYPE_CHECKING:
    from main_window import MyWindow

# Class that inherits from QPushButton and is used to create custom buttons for our calculator
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)

        self.setMinimumSize(75, 75)


# class that inherits from QGridLayout and will have the buttons in calculator format, it has a gridmask attribute that
# has a list with the value that will go on the buttons, then the makeGrid function is called, which will go through this
# list and take the value of the row and column, instantiate a button and check with the isNumOrDot and isEmpty function
# if it is the special button or not, to apply the settings, then this button is added to the grid with its value in the
# proper position (row and column).


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, info: Info, window: 'MyWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self.window = window

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid()


    def _makeGrid(self):
        self.display.setFocus()

        for i, rowData in enumerate(self._gridMask):
            for j, cellData in enumerate(rowData):
                b = Button(cellData)

                if not isNumOrDot(cellData) and not isEmpty(cellData):
                    b.setProperty('cssClass', 'specialButton')

                self.addWidget(b, i, j)





