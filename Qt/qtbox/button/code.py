import sys

from PyQt5.QtCore import Qt, QRectF, QRect
from PyQt5.QtWidgets import QPushButton, QApplication, QGraphicsDropShadowEffect, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor


class QtBoxStyleButton1(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton1, self).__init__()
        self.btn_state = "off"
        self.setFixedSize(80, 40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.NoPen)
        painter.setPen(pen)

        if self.btn_state == "on":
            painter.setBrush(QColor(96, 202, 91))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

            painter.setBrush(Qt.white)
            rect = QRectF(self.width()/2-5, 5, self.width()/2, self.height()-5*2)
            painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

        else:
            painter.setBrush(QColor(220, 220, 220))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

            painter.setBrush(Qt.white)
            rect = QRectF(5, 5, self.width()/2, self.height()-5*2)
            painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.btn_state == "on":
                self.btn_state = "off"
            else:
                self.btn_state = "on"

class QtBoxStyleButton2(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton2, self).__init__()
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)

class QtBoxStyleButton3(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton3, self).__init__()
        self.setFixedSize(150, 50)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #47a7ed, stop: 1 #a967b2);
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 25px;
        }

        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #459ee0, stop: 1 #995da1);
        }

        QPushButton:pressed {
               background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #4093d1, stop: 1 #87538e);
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleButton3()
    checkbox.show()
    sys.exit(app.exec_())