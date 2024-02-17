import time
# 装饰器的应用1
def logincheck(func):
    # 用于验证用户是否登录
    def wrapper(*args, **kwargs):
        print('验证成功')
        func(*args, **kwargs)
    return wrapper

def timedecorate(func):
    # 用于验证时间是否正确
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('时间验证成功', time.time())
    return wrapper

@timedecorate
@logincheck
def say_hello(name, a=1, b=2):
    print('hello', name)
    print(a, b)

# 装饰器的应用2:日志记录,在函数调用前后添加日志记录。
import logging
logging.basicConfig(level=logging.INFO)
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

# 装饰器的应用3:缓存：实现函数结果的缓存。
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_decorator
def slow_function(x):
    time.sleep(2)
    return x * x

# 装饰器的应用4:权限检查：检查用户是否有执行某个函数的权限。
def permission_decorator(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("You do not have permission to perform this action.")
    return wrapper

class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin

@permission_decorator
def restricted_function(user):
    print("Access granted, performing action...")

if __name__ == '__main__':
    say_hello('world')

    # greet("Alice")

    # print(slow_function(2))  # This will take 2 seconds
    # print(slow_function(2))  # This will be instant

    # user = User(is_admin=False) # user = User(is_admin=True)
    # restricted_function(user)  # This will raise a PermissionError