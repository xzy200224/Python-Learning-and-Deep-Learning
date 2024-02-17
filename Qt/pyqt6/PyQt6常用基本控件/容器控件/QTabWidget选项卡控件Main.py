"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QTabWidget, QWidget
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTabWidget选项卡控件.ui")

    myTabWidget: QTabWidget = ui.tabWidget

    tab = QWidget()

    myTabWidget.addTab(tab, "测试")

    tab2 = QWidget()

    myTabWidget.insertTab(1, tab2, QIcon("other.png"), "测试")

    # myTabWidget.removeTab(1)

    print(myTabWidget.currentWidget(), myTabWidget.currentIndex())

    myTabWidget.setCurrentIndex(2)

    myTabWidget.setCurrentWidget(tab2)

    myTabWidget.setTabText(1, "测试222")

    print(myTabWidget.tabText(2))

    ui.show()

    sys.exit(app.exec())
