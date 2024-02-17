import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    # 创建应用必须先实例化一个QApplication，并将sys.argv作为参数传入
    app = QApplication(sys.argv)
    # label = QLabel()
    # label.setText('Hello World')
    label = QLabel('<font color="red">Hello</font> <h1>World</h1>')
    label.show()    # 调用show()方法使控件可见(默认是隐藏)
    sys.exit(app.exec_())   # app.exec_()是执行应用，让应用开始运转循环，直到窗口关闭返回0给sys.exit()，退出整个程序。
