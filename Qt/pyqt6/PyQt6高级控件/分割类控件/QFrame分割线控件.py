# Form implementation generated from reading ui file 'QFrame分割线控件.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 276)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(260, 0, 61, 271))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(100, 50, 53, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(410, 50, 53, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 53, 15))
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(parent=Form)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "设置1"))
        self.label_2.setText(_translate("Form", "设置2"))
        self.label_3.setText(_translate("Form", "设置3"))
