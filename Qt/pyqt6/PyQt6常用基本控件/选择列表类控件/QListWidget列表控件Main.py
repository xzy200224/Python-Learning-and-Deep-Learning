"""
    python加载ui文件
    作者 : 小锋老师
    官网 : www.python222.com
"""
import sys
import time

from PyQt6.QtGui import QValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QTextEdit, QComboBox, QFontComboBox, QListWidget, \
    QListWidgetItem
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QListWidget列表控件.ui")
    myListWidget: QListWidget = ui.listWidget
    lwItem = QListWidgetItem()
    lwItem.setText("进击的巨人 最终季 完结篇 后篇 / Attack on Titan: The Final Season, The Final Chapters - Part 2")
    myListWidget.addItem(lwItem)

    myListWidget.addItem("杀手")
    list = [
        "第八个嫌疑人 / 第8个嫌疑人 / Dust To Dust ",
        "最后的真相 / 隐秘的真相 / Heart's Motive ",
        "坠落的审判 / 坠楼死亡的剖析 / 一场坠楼的剖析",
        "猜谜女士 / 常识女王(台)"
    ]
    myListWidget.addItems(list)

    myListWidget.insertItem(1, "测试插入")

    myListWidget.setCurrentItem(lwItem)

    selectedItemList = myListWidget.selectedItems()

    for item in selectedItemList:
        print(item.text())

    ui.show()

    sys.exit(app.exec())
