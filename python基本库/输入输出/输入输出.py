"""
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
例子：对于一个日期对象，str()可能返回 '2019-06-07'。而 repr() 返回 'datetime.date(2019, 6, 7)'。
"""
for x in range(1, 11):
    # .rjust(2)：返回一个新的字符串，这个字符串是原字符串右对齐，并使用空格填充至指定的宽度。
    # 类似的方法, 如 ljust() 和 center()。
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用:不换行
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    # {}：这是一个占位符，它会被format()方法中的参数替换。
    # 0：这是format()方法中参数的索引，0表示第一个参数。
    # :：这是格式说明符
    # 2d：这是格式化字符串，表示将第一个参数格式化为带符号的两位十进制数。
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# format:位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

import math
# :.3f：这是格式化字符串，表示将浮点数格式化为小数点后保留三位的浮点数。
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# items()是字典（dictionary）的一个方法。items()方法返回一个视图对象，该对象包含字典中的键值对元组。
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 使用方括号 [] 来访问键值
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 读取键盘输入
str = input("请输入：");print ("你输入的内容是: ", str)