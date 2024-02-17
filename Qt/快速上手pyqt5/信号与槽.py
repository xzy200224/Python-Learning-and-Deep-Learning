import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):                                            # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)                # 2
        self.button.clicked.connect(self.change_text)           # 3

    def change_text(self):
        print('change text')
        self.button.setText('Stop')                             # 4
        self.button.clicked.disconnect(self.change_text)        # 5
"""
1. 该类继承QWidget，可以将QWidget看作是一种毛坯房，还没有装修，而我们往其中放入QPushButton、QLabel等控件就相当于在装修这间毛坯房。类似的毛坯房还有QMainWindow和QDialog，之后章节再讲述；

2. 实例化一个QPushButton，因为继承于QWidget，所以self不能忘了(相当于告诉程序这个QPushButton是放在QWidget这个房子中的)；

3. 连接信号与槽函数。self.button就是一个控件，clicked(按钮被点击)是该控件的一个信号，connect()即连接，self.change_text即下方定义的函数(我们称之为槽函数)。所以通用的公式可以是：widget.signal.connect(slot)；

4. 将按钮文本从‘Start’改成‘Stop’；

5. 信号和槽解绑，解绑后再按按钮你会发现控制台不会再输出‘change text’，如果把这行解绑的代码注释掉，你会发现每按一次按钮，控制台都会输出一次‘change text’；

6. 实例化Demo类；

7. 使demo可见，其中的控件自然都可见(除非某控件刚开始设定隐藏)

现在用鸣枪和开跑来分析下上面这个例子：按钮控件是裁判，他鸣枪发出信号(clicked)，change_text()槽函数运行就是选手开跑。
"""

# 多个信号连接同一个槽
class Demo2(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)     # 1
        self.button.released.connect(self.change_text)    # 2

    def change_text(self):
        if self.button.text() == 'Start':                 # 3
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

# 一个信号与另外一个信号连接
class Demo3(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.button.released)  # 1
        self.button.released.connect(self.change_text)     # 2

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

# 一个信号连接多个槽
class Demo4(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 1
        self.setWindowTitle('demo')                             # 2
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)    # 3
        self.button.clicked.connect(self.change_window_title)   # 4

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):                               # 5
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):                              # 6
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()                                               # 6
    demo.show()                                                 # 7
    sys.exit(app.exec_())

