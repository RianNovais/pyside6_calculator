from PySide6.QtWidgets import QApplication, QMainWindow
from style import setup_theme
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup_theme()
    myWindow = QMainWindow()

    myWindow.show()
    app.exec()