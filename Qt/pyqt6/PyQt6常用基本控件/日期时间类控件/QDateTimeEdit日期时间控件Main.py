"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QDateTimeEdit
from PyQt6 import uic, QtCore
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QDateTimeEdit日期时间控件.ui")

    myDateTimeEdit: QDateTimeEdit = ui.dateTimeEdit

    myDateTimeEdit.setDate(QtCore.QDate(2023, 12, 4))
    myDateTimeEdit.setTime(QtCore.QTime(13, 19, 24))

    print(myDateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss"))

    print(myDateTimeEdit.date().toString("yyyy-MM-dd"))

    print(myDateTimeEdit.time().toString("HH:mm:ss"))
    
    ui.show()

    sys.exit(app.exec())
