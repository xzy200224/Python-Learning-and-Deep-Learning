"""
在Python中，特殊成员和魔法方法是指那些以双下划线开始和结束的方法，如__init__、__str__等。这些方法在特定的情况下会被Python自动调用。以下是一些常见的魔法方法：

__init__(self, ...): 构造函数，在创建一个新实例时被调用。
__del__(self): 析构函数，当一个对象将要被系统回收时调用。
__str__(self): 定义当使用print打印对象时，看到的内容。
__repr__(self): 定义当使用repr()函数时，看到的内容。
__eq__(self, other): 定义等于符号的行为。
__ne__(self, other): 定义不等于符号的行为。
__lt__(self, other): 定义小于符号的行为。
__gt__(self, other): 定义大于符号的行为。
__le__(self, other): 定义小于等于符号的行为。
__ge__(self, other): 定义大于等于符号的行为。
__add__(self, other): 定义加法的行为。
__sub__(self, other): 定义减法的行为。
__call__ (self, *args): 使得一个对象实例可以像函数一样被调用。
__len__(self): 定义当被len()调用时的行为。它返回对象的“长度”。这个方法通常在实现了集合类的对象上定义，如列表、元组、字符串等

__getitem__(self, key): 定义获取容器中元素的行为，相当于self[key]。
__setitem__(self, key, value): 定义设置容器中指定元素的行为，相当于self[key] = value。
__delitem__(self, key): 定义删除容器中指定元素的行为，相当于del self[key]。
__iter__(self): 定义获取容器的迭代器的行为。

以下是一些常见的特殊成员：
__name__：模块名称，如果是主程序则返回'__main__'。
__doc__：模块、类、方法或函数的文档字符串。
__class__：实例的类。
__bases__：类的基类组成的元组。
__dict__：模块、类、实例或任何其它对象的属性字典。
__file__：模块的路径。
"""
class Cat:
    """
    定义一个猫类
    """
    instances = []
    def __init__(self, name):
        self.name = name
        self.age = 1
        # 以双下划线__开头的属性被称为私有属性。这些属性只能在类的内部访问，
        # 不能通过对象直接访问。这是一种封装机制，用于隐藏和保护对象的内部状态。
        self.__private_attribute = 0
        # 获取当前实例所属类, 将当前实例添加到 instances 列表
        self.__class__.instances.append(self)

    def __repr__(self):
        return f"Cat({self.name})"

    def __str__(self):
        return '我是' + self.name

    def __del__(self):
        print(f"{self.name} has gone!")

    def meow(self):
        return "Meow!"

    def __call__(self, *args, **kwargs):
        print(f"{self.name} is calling you!")
        print(args)

    def __len__(self):
        return self.age

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __add__(self, other):
        if isinstance(other, Cat):
            return self.age + other.age

    @classmethod
    def remove_instance(cls, name):
        """
        删除指定名称的实例
        """
        for cat in cls.instances:
            if cat.name == name:
                cls.instances.remove(cat)
                del cat
                break



cat = Cat("Blue")
cat2 = Cat("Green")
print(cat)  # 输出：Blue
print(repr(cat))  # 输出：Cat(Blue)
print(cat.__doc__)  # 输出：定义一个猫类
print(cat.__module__)  # 输出：__main__
print(cat.__class__)  # 输出：<class '__main__.Cat'>
cat(1, 2)  # 输出：Blue is calling you!
print(cat.__dict__)  # 输出：{'name': 'Blue', 'age': 1, '_Cat__private_attribute': 0}
print(len(cat))  # 输出：1

# 使用__getitem__方法获取属性值
cat['name'] = 'Red'
print(cat['name'])  # 输出：Red
# del cat['name']
print(cat.__dict__)  # 输出：{'age': 1, '_Cat__private_attribute': 0}
for key in cat:
    print(key)  # 输出：age, _Cat__private_attribute
for cat in Cat.instances:
    print("instances:", cat) # 输出：instances: Cat(Blue), instances: Cat(Green)
cat.remove_instance("Red")


