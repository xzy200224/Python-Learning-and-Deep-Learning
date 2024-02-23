"""
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None,
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)

参数说明：
args： 要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
bufsize： 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
stdin, stdout, stderr： 分别表示程序标准输入、输出、错误句柄。
preexec_fn： 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
close_fds： 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
shell： 该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，则建议将args参数作为一个字符串传递而不要作为一个序列传递。
cwd： 如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
env： 用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。如果env!=None，它的值必须是一个映射对象。
universal_newlines： 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，否则他们将会被作为二进制流被打开。
startupinfo和creationflags： 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如主窗口的外观，进程优先级等。
————————————————
Popen 对象方法:
poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。
wait(timeout): 等待子进程终止。
communicate(input,timeout): 和子进程交互，发送和读取数据。
send_signal(singnal): 发送信号到子进程 。
terminate(): 停止子进程,也就是发送SIGTERM信号到子进程。
kill(): 杀死子进程。发送 SIGKILL 信号到子进程。
"""
import subprocess
# 用法和参数与run()方法基本类同，但是它的返回值是一个Popen对象，而不是CompletedProcess对象。
ret = subprocess.Popen("dir", shell=True)
print(type(ret))

# Popen对象的stdin、stdout和stderr是三个文件句柄，可以像文件那样进行读写操作。
s = subprocess.Popen("ipconfig", stdout=subprocess.PIPE, shell=True)
print(s.stdout.read().decode("gbk"))

s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
s.stdin.write(b"import os\n")
s.stdin.write(b"print(os.environ)")
s.stdin.close()
out = s.stdout.read().decode("GBK")
s.stdout.close()
print(out)

# 通过communicate()方法与子进程进行交互
proc = subprocess.Popen(
    ['wsl', 'echo', '"to stdout"'],    # 在Unix下执行 echo "to stdout" 命令
    stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

proc2 = subprocess.Popen(['wsl', '/bin/bash', '-c', 'echo hello; sleep 10'], stdout=subprocess.PIPE)
try:
    outs, errs = proc2.communicate(timeout=5)
except subprocess.TimeoutExpired:
    # 杀死子进程，并尝试再次调用 communicate 方法来获取任何剩余的输出。
    proc2.kill()
    outs, errs = proc2.communicate()
    print('stdout:', outs.decode('utf-8') if outs else '', 'stderror:', errs.decode('utf-8') if errs else '')
