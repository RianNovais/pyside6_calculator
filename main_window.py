from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout
from info import Info
from display import Display
from buttons import Button, ButtonGrid

# class of the main window, which will have the central widget and the vLayout inserted and inside the vLayout we will
# have the info, which will show the result of the operations, the display, which will show what the user clicks and
# types, and the grid of buttons.
class MyWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('Calculator')

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()

        info = Info('2^2 = 4')
        self.vLayout.addWidget(info)

        display = Display()
        self.vLayout.addWidget(display)

        buttonsGrid = ButtonGrid(display, info, self)
        self.vLayout.addLayout(buttonsGrid)

        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)






