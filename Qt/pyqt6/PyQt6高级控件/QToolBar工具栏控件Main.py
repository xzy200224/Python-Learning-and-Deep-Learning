"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QToolBar工具栏控件.ui")

    myToolBar: QToolBar = ui.toolBar

    myToolBar.addAction(QIcon("add.png"), "新建")

    myToolBar.addSeparator()

    myToolBar.addAction(QIcon("save.png"), "保存")

    ui.show()

    sys.exit(app.exec())
