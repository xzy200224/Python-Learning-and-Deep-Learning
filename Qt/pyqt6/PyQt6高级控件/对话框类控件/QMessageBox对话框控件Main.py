"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QPushButton, QMessageBox
from PyQt6 import uic
import sys


def showInfo():
    # QMessageBox.information(None, '消息对话框标题', '消息对话框内容', QMessageBox.StandardButton.Ok)
    result = QMessageBox.information(None, '消息对话框标题', '消息对话框内容',
                                     QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)
    if result == QMessageBox.StandardButton.Ok:
        print("点了OK")
    elif result == QMessageBox.StandardButton.No:
        print("点了No")
    # QMessageBox.information(None, '消息对话框标题', '消息对话框内容', QMessageBox.StandardButton.Apply)
    # QMessageBox.information(None, '消息对话框标题', '消息对话框内容', QMessageBox.StandardButton.Close)


def showCritical():
    QMessageBox.critical(None, '错误对话框标题', '错误对话框内容', QMessageBox.StandardButton.Ok)


def showQuestion():
    QMessageBox.question(None, '问答对话框标题', '问答对话框内容', QMessageBox.StandardButton.Ok)


def showAbout():
    # 关于对话框不能加按钮
    QMessageBox.about(None, '关于对话框标题', '关于对话框内容')


def showWarning():
    QMessageBox.warning(None, '警告对话框标题', '警告对话框内容', QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QMessageBox对话框控件.ui")

    info_btn: QPushButton = ui.pushButton_2
    critical_btn: QPushButton = ui.pushButton_3
    question_btn: QPushButton = ui.pushButton_4
    about_btn: QPushButton = ui.pushButton_5
    warning_btn: QPushButton = ui.pushButton
    info_btn.clicked.connect(showInfo)
    critical_btn.clicked.connect(showCritical)
    question_btn.clicked.connect(showQuestion)
    about_btn.clicked.connect(showAbout)
    warning_btn.clicked.connect(showWarning)
    ui.show()

    sys.exit(app.exec())
