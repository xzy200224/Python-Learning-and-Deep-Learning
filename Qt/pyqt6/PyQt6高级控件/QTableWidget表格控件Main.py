"""
    
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QValidator, QIntValidator, QIcon, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QToolBar, QStatusBar, QTableWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt6 import uic
import sys
from pymysql import Connection

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./QTableWidget表格控件.ui")

    table: QTableWidget = ui.tableWidget

    con = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="db_pyqt6"
    )
    cursor = con.cursor()
    cursor.execute("select * from t_book")
    result = cursor.fetchall()

    row = cursor.rowcount  # 获取记录数，也就是表格的行数
    vol = len(result[0])  # 获取列数
    con.close()

    table.setRowCount(row)
    table.setColumnCount(vol)
    table.setHorizontalHeaderLabels(['编号', '书名', '类别', '作者', '出版日期', '价格'])

    for i in range(row):
        for j in range(vol):
            if j == 5:
                data = QTableWidgetItem(QIcon("add2.png"), str(result[i][j]))
            else:
                data = QTableWidgetItem(str(result[i][j]))

            if j == 2:
                combobox = QComboBox()
                combobox.addItems(['Python', 'Java', 'Go'])
                combobox.setCurrentIndex(0)
                table.setCellWidget(i, j, combobox)
            else:
                data.setForeground(QBrush(QColor("red")))  # 设置文本颜色
                data.setBackground(QBrush(QColor("yellow")))  # 设置背景颜色
                table.setItem(i, j, data)

    table.resizeColumnsToContents()  # 设置类宽度跟随内容改变
    table.resizeRowsToContents()  # 设置高度跟随内容改变
    table.setAlternatingRowColors(True)  # 设置表格颜色行交错显示
    table.horizontalHeader().setStretchLastSection(True)  # 设置最后一列自动填充表格
    table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 禁止编辑表格单元
    # table.sortItems(4, Qt.SortOrder.DescendingOrder)  # 设置根据第5类数据降序
    # table.setSpan(2, 3, 2, 2)
    ui.show()

    sys.exit(app.exec())
