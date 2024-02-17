"""
生成器（Generators）
生成器是一种特殊的迭代器，它的定义方式与普通函数相似，但使用yield语句返回结果，而不是return。
生成器在每次产生结果后会自动挂起并保存当前的所有信息，等待下一次的调用。
这种特性使得生成器非常适合处理大规模数据或无限序列，因为它们在任何时候都只需要保存有限的状态信息。
"""
# 生成器的定义
from collections.abc import Iterable
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# 判断是否为可迭代对象
numbers = count_up_to(5)
print(isinstance(numbers, Iterable))  # 输出 True

# 使用生成器
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        if count >= n:
            break
        yield a + b
        a, b = b, a + b
        count += 1

nums = fibonacci(10000000000)
for i, num in enumerate(nums):
    if i % 1000 == 0:
        print(num)