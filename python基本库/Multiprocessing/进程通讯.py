import multiprocessing
import time

def task(q):
    for i in range(10):
        q.put(i)

def task2(conn):
    time.sleep(1)
    conn.send([111, 22, 33, 44])
    data = conn.recv()  # 阻塞
    print("子进程接受：", data)
    time.sleep(2)

if __name__ == '__main__':
    # 方法1：queue，单向
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=task, args=(queue,))
    p.start()
    p.join()
    print("主进程")
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())

    # 方法2：pipe，双向
    parent_conn, child_conn = multiprocessing.Pipe()
    p2 = multiprocessing.Process(target=task2, args=(child_conn,))
    p2.start()
    info = parent_conn.recv() # 阻塞
    print("主进程接受：",info)
    parent_conn.send('hello')
