import subprocess

obj = subprocess.Popen('dir',
                 shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

res = obj.stdout.read()
print(res.decode('GBK'))

error_res = obj.stderr.read()
print(error_res.decode('GBK'))