import time
import multiprocessing
import os
def sing(num = 3, name = None):
    # 获得进程编号
    print("唱歌进程的pid:", os.getpid())
    print("唱歌进程的父进程的pid", os.getppid())
    for i in range(num):
        print(f"唱歌{name}")
        time.sleep(0.5)

def dance(y = 3, name = None):
    print("跳舞进程的pid:", os.getpid())
    print("跳舞进程的父进程的pid", os.getppid())
    for i in range(y):
        print(f"跳舞{name}")
        time.sleep(0.5)

if __name__ == "__main__":
    # 获取CPU的个数
    print(multiprocessing.cpu_count())
    print("主进程的pid:", os.getpid())
    # target:函数名;
    # args/kwargs:函数的参数;
    sing_process = multiprocessing.Process(target=sing, args=(5, "情歌"))
    dance_process = multiprocessing.Process(target=dance, kwargs={'y': 5, 'name': "情话"})
    # 设置守护进程,随主进程结束而结束
    # sing_process.daemon = True
    # 启动进程
    sing_process.start()
    dance_process.start()
    # 等待结束
    sing_process.join()
    dance_process.join()

