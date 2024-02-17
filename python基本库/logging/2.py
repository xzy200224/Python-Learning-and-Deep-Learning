import logging

# 向日志输出变量
logging.basicConfig(level=logging.DEBUG)
name = '张三'
logging.debug("姓名 {}".format(name))
