import logging
# 记录器,并设计级别
logger = logging.getLogger("cn.cccb.applog")
logger.setLevel(logging.DEBUG)

# 屏幕handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# 文件handler,使用logger的级别
fileHandler = logging.FileHandler(filename='addDemo.log', mode='w')
fileHandler.setLevel(logging.INFO)

# formatter格式，里面的8，10实现了占位对齐
formatter = logging.Formatter("%(asctime)s|%(levelname)8s|%(filename)s:%(lineno)s|%(message)s", datefmt="%Y-%m-%d %H:%H:%S")

# 给handler设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 记录器要设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 定义一个过滤器
flt = logging.Filter("cn.cccb")
# 关联过滤器
logger.addFilter(flt)   # 其它：fileHandler.addFilter(flt)

# 打印日志的代码
# logging.debug()#不能使用这个了！！！会使用WARNING的版本，不会用之前的记录器
logger.debug("this is debug log")
logger.info("this is info log")
logger.warning("this is warning log")
logger.error("this is error log")
logger.critical("this is critical log")