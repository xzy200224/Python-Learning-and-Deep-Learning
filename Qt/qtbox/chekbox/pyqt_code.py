import sys
from PyQt5.QtWidgets import QCheckBox, QApplication

class QtBoxStyleCheckBox1(QCheckBox):
    def __init__(self):
        super(QtBoxStyleCheckBox1, self).__init__()
        self.setText("No")
        self.toggled.connect(lambda: self.setText("Yes" if self.isChecked() else "No"))
        self.setStyleSheet("""
        QCheckBox {
            font-family: "Microsoft YaHei";
            font-size: 15px;
            color: #268cf0;
        }

        QCheckBox::indicator {
            padding-top: 1px;
            width: 40px;
            height: 30px;
            border: none;
        }

        QCheckBox::indicator:unchecked {
            image: url(开关按钮-关.png);
        }

        QCheckBox::indicator:checked {
            image: url(开关按钮-开.png);
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleCheckBox1()
    checkbox.show()
    sys.exit(app.exec_())

