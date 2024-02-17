import os
# 1.系统相关内容：nt（windows系统），posix：unux系统
print(os.name)
print(os.sep)  # 路径分隔符
print(os.pathsep)   # 环境变量分隔符
print(os.linesep)   # 换行符

# 2.文件和目录
# os.mkdir('test')    # 创建目录
# os.rmdir('test')    # 删除目录
# os.remove('test.txt')   # 删除文件
# os.rename('old.txt', 'new.txt')  # 重命名文件
# print(os.getcwd())  # 获取当前目录
# os.chdir('test')    # 切换目录
# os.stat('test.txt') # 获取文件信息

# os.walk()函数来遍历一个目录及其所有子目录。
# 这个函数会返回一个生成器，每次产生一个三元组，包含当前目录的路径，当前目录下的所有目录名，以及当前目录下的所有文件名。
def print_all_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            # 拼接路径
            print(os.path.join(root, file))
print_all_files('.')

# 分割路径
path = "/home/user/documents/file.txt"
head, tail = os.path.split(path)
name, ext = os.path.splitext(tail)
print(head, tail, name, ext)    # /home/user/documents file.txt file .txt

# 判断是否是绝对路径
print(os.path.isabs('D:/test.txt'))
# 判断文件,文件夹是否存在
print(os.path.exists('D:/test.txt'))
print(os.path.isfile('D:/test.txt'))
print(os.path.isdir('D:/test.txt'))

# 3.执行命令
exit_status = os.system('dir')
print("Exit status:", exit_status)
