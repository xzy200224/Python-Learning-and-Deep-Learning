import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QLabel, QApplication


class QtBoxStyleLineEdit3(QLineEdit):
    def __init__(self, parent = None):
        super(QtBoxStyleLineEdit3, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("Please select a save path")
        self.setFixedSize(180, 30)
        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid lightgray;
            border-radius: 5px;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
            padding-left: 62px;
            padding-right: 5px;
        }
        """)

        self.label = QLabel(self)
        self.label.setText("Qt Box")
        self.label.setFixedSize(60, 30)
        self.label.setStyleSheet("""
        QLabel {
            background-color: #f8f9fb;
            color: black; 
            font-size: 15px;
            padding-left: 3px;
            border: 1px solid lightgray;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        }

        QLabel:hover {
            background-color: #ebecf0;
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("untitled.ui")
    # 展示窗口
    ui.show()
    app.exec()