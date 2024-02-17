import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPushButton, QApplication


class QtBoxStyleLineEdit5(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit5, self).__init__()
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("Enter username")
        self.setFixedSize(150, 30)
        self.setStyleSheet("""
        QLineEdit {
            border-top: none;
            border-left: none;
            border-right: none;
            border-bottom: 1px solid black;
            background-color: transparent;
        }

        QLineEdit:focus {
            border-bottom: 1px solid #2a70f4;
        }
        """)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleLineEdit5()
    checkbox.show()
    sys.exit(app.exec_())