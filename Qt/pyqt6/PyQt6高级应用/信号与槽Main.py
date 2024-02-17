"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QPushButton
from PyQt6 import uic
import sys


def cal(a: int, b: int, lineEdit_3: QLineEdit):
    lineEdit_3.setText(str(a + b))


def style(lineEdit_3: QLineEdit):
    lineEdit_3.setStyleSheet("background-color:red")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./信号与槽.ui")

    lineEdit: QLineEdit = ui.lineEdit
    lineEdit_2: QLineEdit = ui.lineEdit_2
    lineEdit_3: QLineEdit = ui.lineEdit_3
    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(lambda: cal(int(lineEdit.text()), int(lineEdit_2.text()), lineEdit_3))
    pushButton.clicked.connect(lambda: style(lineEdit_3))

    lineEdit_3.setHidden(True)

    ui.show()

    sys.exit(app.exec())
