"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QTextEdit
from PyQt6 import uic, QtGui
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTextEdit多行富文本框控件.ui")

    myTextEdit: QTextEdit = ui.textEdit
    myTextEdit_2: QTextEdit = ui.textEdit_2
    myTextEdit.setTextColor(QtGui.QColor(255, 0, 0))
    myTextEdit.setTextBackgroundColor(QtGui.QColor(255, 255, 0))
    myTextEdit.setPlainText("学python，上python222.com")

    myTextEdit_2.setHtml("学<font color='red'>python</font>，上<a href='http://www.python222.com'>python222.com</a>")

    # myTextEdit.clear()
    # myTextEdit_2.clear()

    print(myTextEdit.toPlainText())
    print(myTextEdit_2.toHtml())

    ui.show()

    sys.exit(app.exec())
