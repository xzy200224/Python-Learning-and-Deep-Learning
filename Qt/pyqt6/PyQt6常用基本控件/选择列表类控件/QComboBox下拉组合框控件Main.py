"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QComboBox下拉组合框控件.ui")

    myComboBox: QComboBox = ui.comboBox

    myComboBox.addItem("足球")

    list = ["篮球", "乒乓球"]

    myComboBox.addItems(list)

    myComboBox.addItem(QIcon("other.png"), "其他")

    print(myComboBox.currentText(), myComboBox.currentIndex())

    print(myComboBox.itemText(2))

    myComboBox.setItemText(1, "篮球2")

    print(myComboBox.count())

    ui.show()

    sys.exit(app.exec())
