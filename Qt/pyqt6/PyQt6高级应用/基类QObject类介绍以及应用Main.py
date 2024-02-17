"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 加载qss样式
    with open("label.qss", "r") as f:
        app.setStyleSheet(f.read())
    ui = uic.loadUi("./基类QObject类介绍以及应用.ui")

    label: QLabel = ui.label
    label_2: QLabel = ui.label_2
    label_3: QLabel = ui.label_3
    label.setProperty("level", "warning")
    label_2.setProperty("level", "error")
    label_3.setProperty("level", "error")

    ui.show()

    sys.exit(app.exec())
