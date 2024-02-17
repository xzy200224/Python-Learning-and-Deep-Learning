"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtCore import QTimer, QDateTime
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QPushButton
from PyQt6 import uic
import sys


def show(label: QLabel):
    time = QDateTime.currentDateTime()
    timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss")
    label.setText(timeDisplay)


def start(timer, label):
    timer.start(1000)
    timer.timeout.connect(lambda: show(label))


def stop(timer: QTimer):
    timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTimer计时器控件.ui")
    print(ui)
    timer = QTimer(ui)

    pushButton: QPushButton = ui.pushButton
    pushButton_2: QPushButton = ui.pushButton_2
    label: QLabel = ui.label

    pushButton.clicked.connect(lambda: start(timer, label))
    pushButton_2.clicked.connect(lambda: stop(timer))
    ui.show()

    sys.exit(app.exec())
