import sys
# 处理python解释器相关的变量和方法

print(sys.version)  # 获取python解释器的版本
print(sys.maxsize)  # 获取python解释器的最大值
print(sys.path)  # 获取python解释器的路径
print(sys.platform)  # 获取python解释器的平台
print(sys.argv)  # 获取python解释器的参数（如终端运行时的参数）

print(sys.getdefaultencoding()) # 获取python解释器的默认编码
print(sys.getfilesystemencoding())  # 获取python解释器的文件系统编码

print(sys.modules) # 获取python解释器的模块
print(sys.getsizeof(1))  # 获取对象的内存占用情况。

print(sys.getrecursionlimit())  # 获取python解释器的递归深度
sys.setrecursionlimit(200)  # 设置python解释器的递归深度

def recursion(n):
    if n == 0:
        return
    recursion(n - 1)
recursion(500)  # 递归深度超过1000会报错（RecursionError: maximum recursion depth exceeded in comparison）

sys.exit(0)  # 退出python解释器（参数为退出码，0表示正常退出，非0表示异常退出）

