import sys

from PyQt5.QtWidgets import QLabel, QApplication


class QtBoxStyleLabel1(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel1, self).__init__()
        self.setText("Recon-All")
        self.setFixedSize(90, 90)
        self.setStyleSheet("""
        QLabel {
            border-radius: 45px;
            border-image: url(brain.jpg)
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleLabel1()
    checkbox.show()
    sys.exit(app.exec_())