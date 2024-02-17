"""
    第一个PyQt6程序
    作者 : 小锋老师
    官网 : www.python222.com
"""
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建一个应用
# print(sys.argv)
# print(app.arguments())

window = QWidget()
window.setWindowTitle("学Python，上python222.com")
window.resize(400, 300)
window.move(100, 300)
window.show()

label = QLabel()
label.setText("Python大爷，你好")
label.move(80, 80)
label.resize(150, 50)
label.setStyleSheet("background-color:yellow;padding:10px")
label.setParent(window)
label.show()

sys.exit(app.exec())  # 开始执行程序，并且进入消息循环等待
