"""
    python加载ui文件
    作者 : 小锋老师
    官网 : www.python222.com
"""
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QInputDialog, QFontDialog, \
    QColorDialog
from PyQt6 import uic, QtGui


def selectColor():
    color, ok = QColorDialog.getColor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QColorDialog颜色对话框控件.ui")

    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(selectColor)

    ui.show()

    sys.exit(app.exec())
