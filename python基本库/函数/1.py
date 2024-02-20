# 不定长参数
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

# 匿名函数
"""
Python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。

语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
"""
x = lambda a : a + 10
print(x(5))

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

"""
用法：
回调函数：当你需要传递一个函数作为另一个函数的参数时，匿名函数很有用。这在异步编程、事件处理、定时器设置等场景中很常见。
简短的函数体：如果函数的实现非常简单，只有一行或几行代码，那么使用匿名函数可以使代码更简洁。
即时执行：如果一个函数只需要执行一次，那么你可以创建一个匿名函数并立即执行它，这样可以避免不必要的函数命名。
闭包和作用域：在某些编程语言中，匿名函数可以访问其外部作用域的变量，这使得它们在处理作用域和闭包问题时非常有用。
函数式编程：在函数式编程中，函数是一等公民，可以像其他值一样被传递和操作。在这种情况下，匿名函数非常常见，特别是在高阶函数（如map、reduce、filter等）的使用中。

map(function, iterable, ...): 这个函数接受一个函数和一个或多个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素，并返回一个与原可迭代对象同样长度的新迭代器。
filter(function, iterable): 这个函数接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素，并返回一个只包含使函数返回值为True的元素的新迭代器。
reduce(function, iterable[, initializer]): 这个函数在Python 3中被移动到了functools模块中。
它接受一个二元函数（接受两个参数的函数）和一个可迭代对象作为参数，然后连续地将函数应用于可迭代对象的元素，从而将可迭代对象减少为单个输出。
"""
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]
print(list(filter(lambda x: True if x % 2 == 0 else False, numbers))) # 输出：[2, 4, 6, 8]

tele = [("Sam", 32), ("Alice", 23), ("Bob", 27)]
tele.sort(key=lambda x: x[1], reverse=True) # 按年龄降序排序
print(tele)  # 输出：[('Sam', 32), ('Bob', 27), ('Alice', 23)]

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出：120

print(reduce(lambda x, y: x + y, range(1, 101)))  # 输出：5050