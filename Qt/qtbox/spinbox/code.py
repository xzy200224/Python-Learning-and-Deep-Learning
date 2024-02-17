import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpinBox, QApplication


class QtBoxStyleSpinBox1(QSpinBox):
    def __init__(self):
        super(QtBoxStyleSpinBox1, self).__init__()
        self.setFixedSize(150, 30)
        self.setCursor(Qt.PointingHandCursor)
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setStyleSheet("""
        QSpinBox {
            border: 1px solid lightgray;
            border-radius: 3px;
        }

        QSpinBox::up-button {
            width: 14px;
            height: 14px;
            margin: 0px 3px 0px -3px;
            border-image: url(collapse-arrow.png);
        }

        QSpinBox::up-button:pressed {
            margin-top: 1px;
        }

        QSpinBox::down-button {
            width: 14px;
            height: 14px;
            margin: 0px 3px 0px -3px;
            border-image: url(expand-arrow.png);
        }

        QSpinBox::down-button:pressed {
            margin-bottom: 1px;
        }
        """)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleSpinBox1()
    checkbox.show()
    sys.exit(app.exec_())