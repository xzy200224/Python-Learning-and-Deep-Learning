import logging

# 输出格式
logging.basicConfig(format="%(asctime)s|%(levelname)8s|%(filename)8s:%(lineno)s|%(message)s",datefmt="%Y-%m-%d %H:%H:%S" ,level=logging.DEBUG)
name = '张三'
age = 15
logging.debug("姓名 {}, 年龄 {}".format(name, age))
