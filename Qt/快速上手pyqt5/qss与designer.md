参考链接：
https://zhuanlan.zhihu.com/p/75673557
https://www.bilibili.com/video/BV11C4y1P7fj?p=1
# qss
## qss基本概念和用法

每条QSS样式都由两部分组成：

1. 选择器，该部分指定要美化的控件

2. 声明，该部分指定要在控件上使用的属性和值

例如下面这条样式：

```python
QPushButton {color: red}
```

QPushButton是设置的选择器，而大括号里的color: red分别为属性和值。这条样式会将所有的QPushButoon实例和它子类的文本颜色都设置为红色。

可以声明多个属性和值，各对属性和值之间用分号分隔：

```python
QPushButton {color: red; background-color: blue}
```

当然也可以同时指定多个选择器：

```python
QPushButton, QLabel, QLineEdit {color: red}
```

++++++

选择器不单单只有上面提到的那种写法，以下表格总结了最常用的几种选择器类型：

| Selector            | 示例                        | 说明                                              |
| ------------------- | --------------------------- | ------------------------------------------------- |
| Universal Selector  | `*`                         | 星号匹配所有的界面元素                            |
| Type Selector       | `QPushButton`               | 选择所有 QPushButton类型 （包括其子类）           |
| Class Selector      | `.QPushButton`              | 选择所有 QPushButton类型 ，但是不包括其子类       |
| ID Selector         | `QPushButton#okButton`      | 选择所有 `对象名为 okButton` 的QPushButton类型    |
| Property Selector   | `QPushButton[flat="false"]` | 选择所有 flat 属性值为 false 的 QPushButton类型。 |
| Descendant Selector | `QDialog QPushButton`       | 选择所有 QDialog `内部` QPushButton类型           |
| Child Selector      | `QDialog > QPushButton`     | 选择所有 QDialog `直接子节点` QPushButton类型     |

例子：

```python
* {color: red} # 所有控件的文本颜色都设为红色
QPushButton {background-color: blue} # 把所有QPushButton实例及其子类的背景颜色设为蓝色
QPushButton[name='btn'] {background-color: green} # 把所有name属性为btn的QPushButton实例的背景色设为绿色
.QLineEdit {font: bold 20px} # 把所有QLineEdit实例(不包括子类)的字体变粗，大小设为15px
QComboBox#cb {color: blue} # 把所有objectName为hello的下拉框文本颜色设为蓝色
QGroupBox QLabel {color: blue} # 把所有包含在QStackedWidget中的QLabel控件的文本颜色设为蓝色(无论直接包含还是间接包含)
QGroupBox > QLabel {font: 30px} # 把所有QStackedWidget直接包含的QLabel文本字体大小设为30px
```

++++

子控件：QComboBox由一个矩形框和一个下拉按钮组成，而这个下拉按钮就是QComboBox的子控件了，PyQt5允许我们使用QSS对其进行样式化。如下：

```python
 qss = """
          QSpinBox::up-button {image: url(up-arrow.png)}
          QSpinBox::down-button {image: url(down-arrow.png)}  
          """
```

伪状态：伪状态选择器可以让我们针对某控件的不同状态进行QSS样式化操作，下面我们以QPushButton和QComboBox为例。

```python
    demo = Demo()
    qss = """
          QPushButton:hover {background-color: red}                     
          QPushButton[name='btn2']:pressed {background-color: blue}
          QComboBox::drop-down:hover {background-color: green}
          """
    demo.setStyleSheet(qss)
```

伪状态选择器写法就是在控件名后加一个英文状态下的冒号:，再加上伪状态即可。以下是对三条QSS样式的解释：

```python
QPushButton:hover {background-color: red} # 当鼠标悬停在QPushButton实例或其子类上时，将背景变为红色                    
QPushButton[name='btn2']:pressed {background-color: blue} # 当鼠标在QPushButton实例或其子类上按下时，将背景变为蓝色(但只针对name属性为btn2的QPushButton实例及子类)
QComboBox::drop-down:hover {background-color: green} # 当鼠标在QComboBox实例或其子类的下拉按钮子控件上
```

我们知道如果在if判断语句中加个感叹号!就表示相反(否)，那我们也可以在伪状态前加上这个感叹号!来表示相反状态。比如：

```python
QPushButton:!hover {background-color: red}
```

那此时这条样式就会这样解释：当鼠标不悬停在QPushButton实例或其子类上时，背景颜色才会是红色。

## 实际应用

### 背景

可以指定某些元素的背景色，像这样

```css
QTextEdit { background-color: yellow }
```

颜色可以使用红绿蓝数字，像这样

```css
QTextEdit { background-color: #e7d8d8 }
```

也可以像这样指定背景图片

```css
QTextEdit {
    background-image: url(gg03.png);
}
```

### 边框

可以像这样指定边框 `border:1px solid #1d649c;`

其中

`1px` 是边框宽度

`solid` 是边框线为实线， 也可以是 `dashed`(虚线) 和 `dotted`（点）

比如

```css
*[myclass=bar2btn]:hover{
	border:1px solid #1d649c;
}
```

边框可以指定为无边框 `border:none`

### 字体、大小、颜色

可以这样指定元素的 文字字体、大小、颜色

```css
*{	
	font-family:微软雅黑;
	font-size:15px;
	color: #1d649c;
}
```

### 宽度、高度

可以这样指定元素的 宽度、高度

```css
QPushButton {	
	width:50px;
	height:20px;
}
```

### margin、padding

可以这样指定元素的 元素的 margin

```css
QTextEdit {
	margin:10px 11px 12px 13px
}
```

分别指定了元素的上右下左margin。

也可以使用 margin-top, margin-right, margin-bottom, margin-left 单独指定 元素的上右下左margin

比如

```css
QTextEdit {
	margin:10px 50px;
	padding:10px 50px;
}
```

# Qt desinger

