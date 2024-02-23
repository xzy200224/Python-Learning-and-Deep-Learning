"""
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None,
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)

参数说明：
args：shell命令，可以是字符串或者序列类型（如：list，元组）

bufsize：缓冲区大小。当创建标准流的管道对象时使用，默认-1。
0：不使用缓冲区
1：表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式
正数：表示缓冲区大小
负数：表示使用系统默认的缓冲区大小。

stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄

preexec_fn：只在 Unix 平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用

shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。

cwd：用于设置子进程的当前目录。

env：用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承。

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
