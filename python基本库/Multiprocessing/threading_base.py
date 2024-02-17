import threading
import time
import os

def sing(num = 3, name = None):
    for i in range(num):
        print(f"唱歌{name}")
        time.sleep(0.5)

def dance(y = 3, name = None):
    for i in range(y):
        print(f"跳舞{name}")
        time.sleep(0.5)

def task():
    # threading.current_thread()获取当前线程的线程对象
    thread = threading.current_thread()
    print(thread)

if __name__ == "__main__":
    """
    线程执行是无序的
    """
    thread_1 = threading.Thread(target=dance, kwargs={'y': 5, 'name': "极乐净土..."})
    thread_2 = threading.Thread(target=sing, kwargs={'num': 5, 'name': "月亮之上..."})
    thread_1.setDaemon(True)
    thread_2.setDaemon(True)
    thread_2.start()
    thread_1.start()
    time.sleep(1)
    print("主线程结束")