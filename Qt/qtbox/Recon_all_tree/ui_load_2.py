import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from recon_tree import Ui_MainWindow
class MainWidow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWidow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidow()
    window.show()
    sys.exit(app.exec_())