"""
语法格式:
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
参数说明：
args：表示要执行的命令。必须是一个字符串，字符串参数列表。
stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。subprocess.PIPE 表示为子进程创建新的管道。subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。另外，stderr 可以合并到 stdout 里一起输出。
timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。
check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹出 CalledProcessError 异常。
encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。
shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令,shell=True时 args 是字符串，否则必须是一个字符串列表。

run 方法调用方式返回 CompletedProcess 实例，和直接 Popen 差不多，实现是一样的，实际也是调用 Popen，与 Popen 构造函数大致相同
"""
"""
subprocess.CompletedProcess
run() 方法的返回值，表示一个进程结束了。CompletedProcess类有下面这些属性：

args 启动进程的参数，通常是个列表或字符串。
returncode 进程结束状态返回码。0表示成功状态。
stdout 获取子进程的 stdout。通常为 bytes 类型序列，None 表示没有捕获值。如果你在调用 run() 方法时，设置了参数stderr=subprocess.STDOUT，则错误信息会和 stdout 一起输出，此时 stderr 的值是 None。
stderr 获取子进程的错误信息。通常为 bytes 类型序列，None 表示没有捕获值。
check_returncode() 用于检查返回码。如果返回状态码不为零，弹出CalledProcessError异常。
"""
# 以下命令为Linux命令，winddows下需下载wsl
import subprocess

# 获取执行结果
# 列出目录中的文件和目录，以及它们的详细信息。-l 表示 "long format"
result = subprocess.run(['wsl', 'ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

# 错误处理
# shell=True时 args 是字符串。
# 'exit 1' 是在 Linux 中执行的命令。exit 是一个 shell 命令，用于结束当前 shell，并返回一个状态码。
# 状态码 0 通常表示成功，非零状态码表示出错。在这个例子中，exit 1 表示结束当前 shell，并返回状态码 1。
# returncode 属性获取子进程的退出状态码
try:
    subprocess.run('wsl exit 1', shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"The command failed with exit code {e.returncode}\n"
          f"ERROR:,{e}")

# 选择捕获输出和错误信息
try:
    completed = subprocess.run(
        "wsl echo Hello; echo error; exit 1",
        shell=True,
        stdout=subprocess.PIPE,
        # 设置 stderr 为 STDOUT，表示错误信息会和标准输出一起输出
        # 使用 DEVNULL 抑制输出流，信息就不会被捕获
        stderr=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )
    print('Have {} bytes in stderr: {!r}'.format(
        len(completed.stderr),
        completed.stderr.decode('utf-16-le', errors='ignore'))
    )