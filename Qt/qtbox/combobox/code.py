import sys

from PyQt5.QtWidgets import QComboBox, QApplication


class QtBoxStyleComboBox2(QComboBox):
    def __init__(self):
        super(QtBoxStyleComboBox2, self).__init__()
        self.setFixedSize(150, 30)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.setStyleSheet("""
        QComboBox {
            background-color: white;
            color: black;
            border: 1px solid lightgray;
            border-radius: 15px;
            padding-left: 15px;
        }

        QComboBox:on {
            border: 1px solid #63acfb;
        }

        QComboBox::drop-down {
            width: 22px;
            border-left: 1px solid lightgray;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QComboBox::drop-down:on {
            border-left: 1px solid #63acfb;
        }

        QComboBox::down-arrow {
            width: 16px;
            height: 16px;
            image: url(down.png);
        }

        QComboBox::down-arrow:on {
            image: url(up.png);
        }

        QComboBox QAbstractItemView {
            color: black;
            border: none;
            outline: none;
            background-color: whitesmoke;
        }

        QComboBox QScrollBar:vertical {
            width: 2px;
            background-color: white;
        }

        QComboBox QScrollBar::handle:vertical {
            background-color: #b2bdaf;
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleComboBox2()
    checkbox.show()
    sys.exit(app.exec_())
