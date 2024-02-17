"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtGui import QValidator, QIntValidator, QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QTreeView
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTreeView树视图.ui")

    myTreeView: QTreeView = ui.treeView

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['分类', '书名', '作者', '价格'])

    bookType1 = QStandardItem('Java类')  # 添加一节节点
    bookType1.appendRow(
        [QStandardItem(''), QStandardItem('Java编程思想'), QStandardItem('艾可儿'), QStandardItem('111')])  # 添加二级节点
    bookType1.appendRow(
        [QStandardItem(""), QStandardItem('Java从入门到精通'), QStandardItem('码牛逼'), QStandardItem('99')])  # 添加二级节点
    model.appendRow(bookType1)

    bookType2 = QStandardItem('Python类')  # 添加一节节点
    bookType2.appendRow(
        [QStandardItem(""), QStandardItem('Python编程思想'), QStandardItem('老王'), QStandardItem('10')])  # 添加二级节点
    bookType2.appendRow(
        [QStandardItem(""), QStandardItem('Python跟我学'), QStandardItem('老六'), QStandardItem('20')])  # 添加二级节点
    model.appendRow(bookType2)

    bookType3 = QStandardItem('Go类')  # 添加一节节点
    bookType3.appendRow(
        [QStandardItem(""), QStandardItem('Go编程思想'), QStandardItem('老王'), QStandardItem('10')])  # 添加二级节点
    model.appendRow(bookType3)

    myTreeView.setModel(model)

    myTreeView.expandAll()
    ui.show()

    sys.exit(app.exec())
