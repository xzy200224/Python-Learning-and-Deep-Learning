# Form implementation generated from reading ui file 'QDateTimeEdit日期时间控件.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 100, 194, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 11, 3), QtCore.QTime(3, 11, 44)))
        self.dateTimeEdit.setDate(QtCore.QDate(2023, 11, 3))
        self.dateTimeEdit.setTime(QtCore.QTime(3, 11, 44))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.Section.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dateTimeEdit.setDisplayFormat(_translate("Form", "yyyy-MM-dd HH:mm:ss"))
