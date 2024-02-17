"""
Python中的推导式（Comprehensions）是一种简洁、易读的方式，
用于创建新的列表（List Comprehensions）、字典（Dictionary Comprehensions）、集合（Set Comprehensions）或生成器（Generator Comprehensions）。
推导式是从一个或多个迭代器快速、简洁地创建数据结构的一种方法。
"""
# 列表推导式（List Comprehensions）
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)
# 字典推导式（Dictionary Comprehensions）
names = ['Alice', 'Bob', 'Charlie']
lengths = {name: len(name) for name in names}
print(lengths)
# 集合推导式（Set Comprehensions）
numbers = [1, 2, 3, 4, 5, 5, 5]
unique_squares = {n**2 for n in numbers}
print(unique_squares)
# 生成器推导式（Generator Comprehensions）
numbers = [1, 2, 3, 4, 5]
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)
# 多重循环推导式
res = [x + y for x in 'abc' for y in '123']
print(res)