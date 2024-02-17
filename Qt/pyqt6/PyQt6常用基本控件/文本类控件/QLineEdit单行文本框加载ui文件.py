"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QLineEdit单行文本框.ui")

    myLineEdit: QLineEdit = ui.lineEdit
    myLineEdit_2: QLineEdit = ui.lineEdit_2

    # print(QValidator.__subclasses__())
    myLineEdit.setValidator(QIntValidator())

    # print(myLineEdit.text())
    # myLineEdit.clear()
    # myLineEdit_2.setFocus()

    ui.show()

    sys.exit(app.exec())
