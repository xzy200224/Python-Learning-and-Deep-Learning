# 字符串·
print("{:s}".format("Hello, World!"))
print("|{:20s}|".format("Hello, World!")) # 占位，默认左对齐
print("|{:>20s}|".format("Hello, World!")) # 右对齐
print("|{:20.2s}|".format("Hello, World!")) # 截断
print("|{:+^20s}|".format("Hello, World!")) # 加号填充

# 数值型 d x o b
print("|{:10d}|".format(42))    # 默认右对齐
print("|{:0^10d}|".format(42))   # 0填充
print("|{0:d}|{0:x}|{0:o}|{0:b}|".format(42)) # 十进制、十六进制、八进制、二进制

print("|{:+d}|{:+d}|".format(42, -42)) # 显示正负号
print("|{:-d}|{:-d}|".format(42, -42)) # 只显示负号
print("|{: d}|{: d}|".format(42, -42)) # 正数显示空格

# 浮点型 f
print("|{:f}|".format(3.141592653589793)) # 默认保留6位小数
print("|{:.2f}|".format(3.141592653589793)) # 保留2位小数
print("|{:20.2f}|".format(3.141592653589793)) # 右对齐

# 千位分隔符
print("|{:,}|".format(1234567890))
# 百分比
print("|{:.2%}|".format(0.25))
# 指数
print("|{:e}|".format(1000000))

# 字符串格式化
print("|{!r}|".format("Hello, World!")) # repr()格式化
print("|{!s}|".format("Hello, World!")) # str()格式化
print("|{!a}|".format("Hello, World!")) # ascii()格式化

# 关键字参数
print("|{name} {age}|".format(name="Alice", age=18))

# 元组
coord = (3, 5)
print("|X: {0[0]}; Y: {0[1]}|".format(coord))

# 字典
point = {'x': 3, 'y': 5}
print("|X: {x}; Y: {y}|".format(**point))

# f字符串,同上
x = 3
y = 5.0123456789
print(f"|X: {x:5d}; Y: {y:.2f}|")