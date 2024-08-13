from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.setText)

    def setText(self):
        self.ui.label.setText("Button Clicked!")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
