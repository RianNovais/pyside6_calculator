from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtGui import QIcon

from variables import WINDOW_ICON_DIR
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

        info = Info('')
        self.vLayout.addWidget(info)

        display = Display()
        self.vLayout.addWidget(display)

        buttonsGrid = ButtonGrid(display, info, self)
        self.vLayout.addLayout(buttonsGrid)

        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.adjustSize()

        #add fixedsize to window / avoid resizing
        self.setFixedSize(self.width(), self.height())

        #adding icon to window
        self.icon = QIcon(str(WINDOW_ICON_DIR))
        self.setWindowIcon(self.icon)






