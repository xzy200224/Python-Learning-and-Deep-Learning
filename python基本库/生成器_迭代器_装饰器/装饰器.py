"""
装饰器（Decorators）

装饰器是Python中的一个高级特性，它们是修改其他函数或类的行为的一种方式。
装饰器本质上是一个接受函数或类并返回函数或类的函数。新的函数通常会在调用原函数之前和或之后执行一些额外的代码，
它们可以帮助你使代码更简洁，也可以实现诸如日志记录、计时、缓存等功能。
"""
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

"""
在这个示例中，my_decorator是一个装饰器，它接受一个函数func作为参数，并定义了一个新的函数wrapper。wrapper函数在调用func之前和之后打印一些消息。然后，my_decorator返回wrapper函数。
@my_decorator语法是应用装饰器的一种方式。在这个例子中，它将say_hello函数作为参数传递给my_decorator，然后将返回的wrapper函数赋值给say_hello。因此，当我们调用say_hello()时，实际上是在调用wrapper()。
装饰器可以用在许多场合，例如：
日志记录：你可以使用装饰器在函数调用前后添加日志记录，以跟踪函数的执行。
计时：你可以使用装饰器来测量函数的执行时间，以便进行性能分析。
缓存：你可以使用装饰器来实现函数结果的缓存，以提高性能。
权限检查：你可以使用装饰器来检查用户是否有执行某个函数的权限。
"""
say_hello()
print(say_hello.__name__)  # wrapper

# 由于say_hello实际上是wrapper函数，所以它的__name__属性是'wrapper'，而不是'say_hello'。这可能会导致一些问题，因为一些代码可能会依赖于函数的__name__属性。
# 为了解决这个问题，Python提供了一个functools.wraps装饰器，它可以将原函数的元信息复制到装饰器函数中。只需要在wrapper函数上添加@functools.wraps(func)即可。
import functools
def my_decorator2(func):
    @functools.wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator2
def say_hello2():
    print("Hello!")

say_hello2()
print(say_hello2.__name__)
# 现在，say_hello的__name__属性是'say_hello'，因为functools.wraps将原函数的元信息复制到了wrapper函数中。

# 装饰器也可以接受参数。在这种情况下，需要编写一个返回装饰器的函数。例如：
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("World")
# 在这个示例中，repeat是一个返回装饰器的函数。它接受一个参数num_times，并返回一个装饰器decorator_repeat。decorator_repeat接受一个函数

# 类属性中的装饰器：装饰器也可以用在类的方法上。在这种情况下，装饰器函数的第一个参数通常是self，表示类的实例。例如：
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property   # 用于将一个方法转换为只读属性
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter  # 用于定义一个属性的setter方法。在Python中,将一个方法转换为可写属性
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius ** 2

    def cylinder_volume(self, height):
        """Calculate volume of a cylinder with this circle as a base"""
        return self.area * height


    # @classmethod：这是一个内置装饰器，用于将一个方法转换为类方法。
    # 类方法是绑定到类而非实例的方法。类方法的第一个参数是类本身，通常命名为cls。
    # 类方法可以被类本身调用，也可以被类的实例调用。
    @classmethod
    def pi(cls):
        return 3.1415926535
print(Circle.pi())  # 3.1415926535
circle = Circle(3)
print(circle.area)
circle.radius = 2
print(circle.area)
