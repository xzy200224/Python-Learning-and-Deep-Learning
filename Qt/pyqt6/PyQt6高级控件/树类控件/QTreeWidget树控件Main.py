"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QValidator, QIntValidator, QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QTreeView, QTreeWidget, \
    QTreeWidgetItem
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTreeWidget树控件.ui")

    myTreeWidget: QTreeWidget = ui.treeWidget

    myTreeWidget.setHeaderLabels(['分类', '书名', '作者', '价格'])

    bookType1 = QTreeWidgetItem(myTreeWidget)  # 创建一级节点
    bookType1.setText(0, "Java类")
    bookType1.setIcon(0, QIcon('type.png'))

    bookType1Child1 = QTreeWidgetItem(bookType1)
    bookType1Child1.setText(0, '')
    bookType1Child1.setText(1, 'Java编程思想')
    bookType1Child1.setText(2, '艾可儿')
    bookType1Child1.setText(3, '109')
    bookType1Child1.setCheckState(1, Qt.CheckState.Unchecked)  # 为节点设置复选框，默认不选中

    bookType1Child2 = QTreeWidgetItem(bookType1)
    bookType1Child2.setText(0, '')
    bookType1Child2.setText(1, 'Java从入门到精通')
    bookType1Child2.setText(2, '码牛逼')
    bookType1Child2.setText(3, '99')
    bookType1Child2.setCheckState(1, Qt.CheckState.Unchecked)  # 为节点设置复选框，默认不选中

    bookType2 = QTreeWidgetItem(myTreeWidget)  # 创建一级节点
    bookType2.setText(0, "Python类")
    bookType2.setIcon(0, QIcon('type.png'))

    bookType2Child1 = QTreeWidgetItem(bookType2)
    bookType2Child1.setText(0, '')
    bookType2Child1.setText(1, 'Python编程思想')
    bookType2Child1.setText(2, '万3')
    bookType2Child1.setText(3, '77')
    bookType2Child1.setCheckState(1, Qt.CheckState.Unchecked)  # 为节点设置复选框，默认不选中

    bookType2Child2 = QTreeWidgetItem(bookType2)
    bookType2Child2.setText(0, '')
    bookType2Child2.setText(1, 'Python从入门到精通')
    bookType2Child2.setText(2, '说说的')
    bookType2Child2.setText(3, '76')
    bookType2Child2.setCheckState(1, Qt.CheckState.Unchecked)  # 为节点设置复选框，默认不选中

    bookType3 = QTreeWidgetItem(myTreeWidget)  # 创建一级节点
    bookType3.setText(0, "Go类")
    bookType3.setIcon(0, QIcon('type.png'))

    bookType3Child1 = QTreeWidgetItem(bookType3)
    bookType3Child1.setText(0, '')
    bookType3Child1.setText(1, 'Go编程思想')
    bookType3Child1.setText(2, 'ss说')
    bookType3Child1.setText(3, '77')
    bookType3Child1.setCheckState(1, Qt.CheckState.Unchecked)  # 为节点设置复选框，默认不选中

    myTreeWidget.setAlternatingRowColors(True)  # 设置斑马线 交替间隔 灰白间隔

    myTreeWidget.expandAll()

    ui.show()

    sys.exit(app.exec())
