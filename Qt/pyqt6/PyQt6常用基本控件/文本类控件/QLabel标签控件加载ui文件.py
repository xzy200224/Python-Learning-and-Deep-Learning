"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./PyQt6常用基本控件.ui")

    myLabel: QLabel = ui.label
    print(myLabel.text())

    ui.show()

    sys.exit(app.exec())
