import time
import multiprocessing

def task(lock):
    print("开始")
    # 加锁
    lock.acquire()
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_number = int(f.read())
    print("排队抢票")
    time.sleep(0.5)
    current_number -= 1
    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_number))
    # 释放锁
    lock.release()
    # 或用 with lock:形式

if __name__ == "__main__":
    # 设置模式
    multiprocessing.set_start_method('spawn')

    # 创建进程锁(.Lock()不允许嵌套，.RLock()允许嵌套)
    lock = multiprocessing.Lock()

    process_list = []

    # 创建并启动进程，并传入锁
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()