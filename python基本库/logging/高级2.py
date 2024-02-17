import logging
import logging.config

# 使用配置文件配置
logging.config.fileConfig('logging.conf', encoding='utf-8')
#使用字典就能从任意格式文件进行配置，字典是一种接口格式
# logging.config.dictConfig({"loggers":"root,applog"})


rootLogger = logging.getLogger()
rootLogger.debug("This is root Logger, debug")

logger = logging.getLogger('applog')
logger.debug("This is applog, debug")

a = 'abc'
try:
    int(a)
except Exception as e:
    logger.exception(e)