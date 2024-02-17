import multiprocessing
import os
import threading

def copy_work(file_name, source_dir, tagert_dir):
    """
    复制文件
    :param file_name:文件名
    :param source_dir:原目录
    :param tagert_dir:目标目录
    """
    source_file = source_dir + '/' + file_name
    target_file = tagert_dir + '/' + file_name
    with open(source_file, 'rb') as  source_f:
        with open(target_file, 'wb') as target_f:
            while True:
                data = source_f.read(1024)
                if data:
                    target_f.write(data)
                else:
                    break
    source_f.close()
    target_f.close()

if __name__ == '__main__':
    source_dir = "C:/Users/Xiangzy/Pictures/Screenshots"
    tagert_dir = "D:/PyCharm/workspace/Project/Multiprocessing/pic"

    try:
        os.mkdir(tagert_dir)
    except:
        print("目标文件已存在")

    file_list = os.listdir(source_dir)
    print(file_list)
    print(source_dir, "------->", tagert_dir)
    thread_list = []
    for file in file_list:
        thread = threading.Thread(target=copy_work,
                                          kwargs={"file_name": file, "source_dir": source_dir, "tagert_dir": tagert_dir})
        thread.start()
        thread_list.append(thread)

    # 等待所有线程执行完成
    for t in thread_list:
        t.join()

    # 所有线程执行完成后，可以进行其他操作
    print("所有文件复制完成")
