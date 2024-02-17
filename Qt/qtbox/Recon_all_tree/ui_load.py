import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("Recon_all_window.ui")
    ui.show()
    app.exec()
