import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
def task(num):
    print(f'Task {num} started')
    time.sleep(2)
    return num

def done(res):
    print(multiprocessing.current_process().pid)
    time.sleep(1)
    print(res.result())
    time.sleep(1)

def task2(lock):
    print("开始")
    # lock.acquire()
    # lock.relase()
    with lock:
        with open('f1.txt', mode='r', encoding='utf-8') as f:
            current_number = int(f.read())
        print("排队抢票")
        time.sleep(0.5)
        current_number -= 1
        with open('f1.txt', mode='w', encoding='utf-8') as f:
            f.write(str(current_number))


if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # 进程池使用锁,不能用multiprocessing.RLock(
    manager = multiprocessing.Manager()
    lock_object = manager.Lock()
    for i in range(10):
        fur = pool.submit(task, i)
        # 回调函数,由主进程处理
        fur.add_done_callback(done)
        # pool.submit(task2, lock_object)
    # 执行完往下执行
    pool.shutdown(True)

    print("结束")