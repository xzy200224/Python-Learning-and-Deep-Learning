"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QPushButton, QMessageBox, \
    QInputDialog
from PyQt6 import uic
import sys


def getName(formLayoutWidget, name_input):
    name, ok = QInputDialog.getText(formLayoutWidget, "姓名", "请输入姓名", QLineEdit.EchoMode.Normal, "python222")
    if ok:
        name_input.setText(name)


def getGrade(formLayoutWidget, grade_input):
    grade, ok = QInputDialog.getItem(formLayoutWidget, "班级", "请选择班级", ('大一1班', '大一2班', '大一3班'), 0,
                                     False)
    if ok:
        grade_input.setText(grade)


def getAge(formLayoutWidget, age_input):
    age, ok = QInputDialog.getInt(formLayoutWidget, "年龄", "请选择年龄", 18, 1, 100, 1)
    if ok:
        age_input.setText(str(age))


def getScore(formLayoutWidget, score_input):
    score, ok = QInputDialog.getDouble(formLayoutWidget, "分数", "请选择分数", 98.5, 0, 100, 2)
    if ok:
        score_input.setText(str(score))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QInputDialog输入对话框控件.ui")
    formLayoutWidget = ui.formLayoutWidget
    name_input: QLineEdit = ui.lineEdit
    name_input.returnPressed.connect(lambda: getName(formLayoutWidget, name_input))

    grade_input: QLineEdit = ui.lineEdit_3
    grade_input.returnPressed.connect(lambda: getGrade(formLayoutWidget, grade_input))

    age_input: QLineEdit = ui.lineEdit_2
    age_input.returnPressed.connect(lambda: getAge(formLayoutWidget, age_input))

    score_input: QLineEdit = ui.lineEdit_4
    score_input.returnPressed.connect(lambda: getScore(formLayoutWidget, score_input))

    ui.show()

    sys.exit(app.exec())
