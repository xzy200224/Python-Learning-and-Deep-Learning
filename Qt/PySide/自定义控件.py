from PySide6 import QtGui, QtWidgets


class QOutlet(QtWidgets.QWidget):
    """
    插座控件
    """

    def __init__(self, parent, color) -> None:
        super().__init__(parent)

        self.color = color
        # 控件设置为固定大小
        self.setMinimumSize(70, 70)
        self.setMaximumSize(70, 70)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        # 画插座边框，细线条
        pen = QtGui.QPen()
        pen.setWidth(1)

        pen.setColor(QtGui.QColor(self.color))
        painter.setPen(pen)
        painter.drawRect(0, 0, 60, 60)

        # 画插孔线条，组线条
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(self.color))
        painter.setPen(pen)

        painter.drawLine(12, 10, 12, 25)
        painter.drawLine(30, 10, 30, 25)
        painter.drawLine(48, 10, 48, 25)

        painter.drawLine(10, 35, 20, 50)
        painter.drawLine(50, 35, 40, 50)

        painter.end()


app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.resize(500, 500)

# 创建第1个插座实例
my = QOutlet(window, 'green')
my.move(0, 0)

# 创建第2个插座实例
my = QOutlet(window, 'red')
my.move(100, 0)

# 创建第3个插座实例
my = QOutlet(window, 'blue')
my.move(200, 0)

window.show()
app.exec()