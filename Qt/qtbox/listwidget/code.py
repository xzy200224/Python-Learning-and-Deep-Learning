import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QApplication


class QtBoxStyleListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxStyleListWidget1, self).__init__()
        self.setFixedSize(200, 200)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        for i in range(10):
            item = QListWidgetItem()
            item.setText(str(i))
            self.addItem(item)

        self.setStyleSheet("""
        QListView {
            border: none;
            background-color: #edeef3;
        }

        QListView::item {
            height: 40px;
            margin: 5px 5px 5px 5px;
            background-color: white;
            border-radius: 6px;
        }

        QListView::item:hover{
            background-color: whitesmoke;
        }

        QListView::item:selected{
            color: black;
            border: 1px solid lightgray;
        }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkbox = QtBoxStyleListWidget1()
    checkbox.show()
    sys.exit(app.exec_())