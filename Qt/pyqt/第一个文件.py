"""
QtCore:包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用
QtGui:包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类
QtWidgets:包含了一些列创建桌面应用的UI元素
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")
    # 纯文本
    label = QLabel("账号", w)
    label.setGeometry(20, 20, 30, 20)
    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)
    # 在窗口里面添加控件
    btn = QPushButton("注册", w)
    btn.setGeometry(50, 80, 70, 30)
    # 窗口的大小
    w.resize(300, 300)
    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width / 2), int(y - height / 2))
    # 展示窗口
    w.show()
    # 程序进行循环等待状态
    app.exec()
