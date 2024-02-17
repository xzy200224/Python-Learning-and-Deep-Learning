"""
*args 表示接受任意数量的位置参数（Positional Arguments）。这意味着你可以向函数传递多个参数，而不需要提前定义参数的数量。在函数内部，这些位置参数会被当作一个元组（tuple）来处理。
**kwargs 表示接受任意数量的关键字参数（Keyword Arguments）。这允许你向函数传递任意数量的键值对作为参数，而不需要提前定义这些键值对。在函数内部，这些关键字参数会被当作一个字典（dict）来处理。
"""
def say_hello(*args, **kwargs):
    for arg in args:
        print(f"Hello, {arg}!")

    for key, value in kwargs.items():
        print(f"{key} says hello to {value}!")

# 调用函数
say_hello("Alice", "Bob", Alice="Sam", Bob="Linda")