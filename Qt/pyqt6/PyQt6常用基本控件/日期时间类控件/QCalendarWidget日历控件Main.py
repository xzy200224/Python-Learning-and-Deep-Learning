"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QDateTimeEdit, QCalendarWidget
from PyQt6 import uic, QtCore
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QCalendarWidget日历控件.ui")

    myCalendarWidget: QCalendarWidget = ui.calendarWidget

    print(myCalendarWidget.selectedDate().toString("yyyy-MM-dd"))

    ui.show()

    sys.exit(app.exec())
