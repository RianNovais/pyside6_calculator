
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING
from display import Display
from PySide6.QtCore import Slot, Qt
from info import Info
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from pathlib import Path
from PySide6.QtWidgets import QWidget

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

    def __init__(self, display: Display,info: Info, window: 'MyWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask_ = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display

        self.info = info

        self.window = window

        self._left = None
        self._right = None
        self._op = None
        self._initial_equation_text = 'My Calculation'

        self._equation = ''
        self._makeGrid_()
        self.display.setFocus()

        self.equation = self._initial_equation_text

    @property
    def equation(self):
        return self._equation
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)


    def _makeGrid_(self):


        self.display.setFocus()
        self.display.enterPressed.connect(self._equalButton)


        self.display.backspacePressed.connect(self.display.backspace)


        self.display.escPressed.connect(self._clear)

        self.display.setFocus()

        for i, rowData in enumerate(self._gridMask_):
            for j, cellData in enumerate(rowData):
                b = Button(cellData)


                if not isNumOrDot(cellData) and not isEmpty(cellData):

                    b.setProperty('cssClass', 'specialButton')

                    self.configSpecialButton(b)


                self.addWidget(b, i, j)


                buttonSlot = self.makeSlot(
                    self.insertButtonTextToDisplay,
                    b
                )


                b.clicked.connect(buttonSlot)


    def makeSlot(self, func, button):

        def realSlot():
            func(button)
        return realSlot


    def _showError(self, text):

        msgBox = self.window.makeMsgBox()
        msgBox.setWindowTitle('')
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        self.display.setFocus()
        msgBox.exec()




    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()

    def insertButtonTextToDisplay(self, button):

        text = button.text()

        new_display_content = self.display.text() + text


        if not isValidNumber(new_display_content):
            return
        self.display.insert(text)
        self.display.setFocus()

    def configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            button.clicked.connect(self._clear)

        if text in "+-/*":
            button.clicked.connect(self.makeSlot(self._operatorClicked, button))

        if text == "=":
            button.clicked.connect(self._equalButton)

        if text == "^":
            button.clicked.connect(self.makeSlot(self._operatorClicked, button))

        if text == "◀":
            button.clicked.connect(self.display.backspace)

        if text == "":
            return

        self.display.setFocus()


    def _clear(self):
        print('Limpou o display')
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._initial_equation_text
        self.display.clear()
        self.display.setFocus()


    def _operatorClicked(self, button: Button):

        displayText = self.display.text()
        buttonText = button.text()

        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('left number not defined')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText

        self.equation = f'{self._left} {self._op} ??'
        self.display.setFocus()

    def _equalButton(self):


        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Enter a valid number')
            return

        if self._right is None:
            self._right = float(displayText)


        self.equation = f'{self._left} {self._op} {self._right}'
        result = ""


        try:

            if '^' in self.equation:
                result = eval(self.equation.replace("^", "**"))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('impossible to divide by 0')
            self._clear()
        except OverflowError:
            self._showError("error number too large")
        except SyntaxError:
            self._showError('unknown error')
            self._clear()


        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self.display.setFocus()
        self._left = result
        self._right = None






