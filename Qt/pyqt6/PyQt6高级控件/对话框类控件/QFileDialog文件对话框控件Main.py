"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QPushButton, QMessageBox, \
    QFileDialog
from PyQt6 import uic
import sys


def selectFile():
    fd = QFileDialog()
    fd.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
    fd.setDirectory('c:\\')  # 设置初始化路径
    fd.setNameFilter('图片文件(*.jpg *.png *.bmp *.ico *.gif)')
    if fd.exec():
        print(fd.selectedFiles())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QFileDialog文件对话框控件.ui")

    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(selectFile)
    ui.show()

    sys.exit(app.exec())
