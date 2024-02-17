"""
迭代器（Iterators）
迭代器是一种对象，它定义了一个__next__()方法，可以在一系列值之间进行迭代。
当你在循环中使用for语句，或者使用函数如list()、sum()等，
Python内部实际上是调用了迭代器的__next__()方法。
当迭代器中没有更多的值时，__next__()方法会抛出StopIteration异常。
"""
# 创建一个迭代器
numbers = iter([1, 2, 3, 4, 5])
print(next(numbers))  # 输出 1
print(next(numbers))  # 输出 2

# 判断是否为可迭代对象
from collections.abc import Iterable
print(isinstance(numbers, Iterable))  # 输出 True

# 自定义迭代器    class __iter__ __next__