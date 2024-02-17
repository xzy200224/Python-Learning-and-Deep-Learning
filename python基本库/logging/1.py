import logging
# 默认日志输出级别为waringing
# 使用baseConfig()来指定日志输出级别
print("this is print log")
logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")
# 输出顺序不一致，不要混用
