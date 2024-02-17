"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QTabWidget, QWidget, QToolBox
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QToolBox工具盒控件.ui")

    myToolBox: QToolBox = ui.toolBox

    tab1 = QWidget()

    myToolBox.addItem(tab1, "测试")

    tab2 = QWidget()

    myToolBox.insertItem(2, tab2, QIcon("4.png"), "测试2223")

    myToolBox.setCurrentIndex(2)

    myToolBox.setItemIcon(0, QIcon('other.png'))

    myToolBox.setItemText(0, "我的好友222")

    myToolBox.setItemEnabled(2, False)

    # myToolBox.removeItem(4)

    print(myToolBox.currentIndex())

    print(myToolBox.itemText(3))

    ui.show()

    sys.exit(app.exec())
