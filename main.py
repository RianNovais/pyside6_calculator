from PySide6.QtWidgets import QApplication
from main_window import MyWindow
from style import setup_theme

import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup_theme()
    myWindow = MyWindow()
    myWindow.show()
    app.exec()