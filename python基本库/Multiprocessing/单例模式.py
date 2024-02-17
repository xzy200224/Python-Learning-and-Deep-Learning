import threading
import time

lock = threading.RLock()

class Singleton:
    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with lock:
            cls.instance = object.__new__(cls)
            return cls.instance

def task():
    obj = Singleton(name="x")
    print(obj)

if __name__ == "__main__":
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()