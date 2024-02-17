import time
# 内容：时间戳 结构化时间对象 格式化时间字符串

# 1.时间戳: 从1970年1月1日0时0分0秒到现在的秒数
print(time.time())# 获取当前时间戳

# 2.结构化时间对象: 用元组表示时间,(tm_year=2024, tm_mon=2, tm_mday=17,....)
st = time.localtime()
print(st, type(st))
# st一共9个元素
print("金泰你是{}年{}月{}日{}时{}分{}秒".format(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec))

# 3.格式化时间字符串
print(time.ctime())  # 获取当前时间的字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", st))  # 格式化时间字符串,可自行定义格式

# 4.程序睡眠
time.sleep(3)  # 程序睡眠3秒
"""
程序运行时间：
start = time.time()
代码块
end = time.time()
print(end - start)
"""

# UTC时间
print(time.gmtime())  # 获取UTC时间
# 本地时间， 将一个时间戳转换为一个代表本地时间的time.struct_time对象。
# 如果没有提供参数，那么将使用time.time()的结果。
print(time.localtime())  # 获取本地时间

# time.strftime(format[, t]): 将一个代表时间的time.struct_time对象转换为一个字符串，
# 该字符串的格式由参数format决定。
t = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
# time.strptime(string[, format]): 将一个时间字符串解析为一个time.struct_time对象。
s = "2024-02-17 10:56:59"
t = time.strptime(s, "%Y-%m-%d %H:%M:%S")