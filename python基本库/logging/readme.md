参考视频：https://www.bilibili.com/video/BV1sK4y1x7e1/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=c52a6491548814d54a99f3b97b0df55c
# 预备知识
## 什么是日志
日志是一种可以追踪某些软件运行时所发生事件的方法。软件开发人员可以向他们的代码中调用日志记录相关的方法来表明发生了某些事情。一个事件可以用一个可包含可选变量数据的消息来描述。此外，事件也有重要性的概念，这个重要性也可以被称为严重性级别（level）。

## 日志的等级

| 级别      | 何时使用                                                     |
| :-------- | :----------------------------------------------------------- |
| DEBUG     | 详细信息，典型地调试问题时会感兴趣。 详细的debug信息。       |
| INFO      | 证明事情按预期工作。 关键事件。                              |
| WARNING   | 表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。 |
| ERROR     | 由于更严重的问题，软件已不能执行一些功能了。 一般错误消息。  |
| CRITICAL  | 严重错误，表明软件已不能继续运行了。                         |
| NOTICE    | 不是错误，但是可能需要处理。普通但是重要的事件。             |
| ALERT     | 需要立即修复，例如系统数据库损坏。                           |
| EMERGENCY | 紧急情况，系统不可用（例如系统崩溃），一般会通知所有用户。   |

# logging的日志等级

| 日志等级（level） | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| DEBUG             | 最详细的日志信息，典型应用场景是 问题诊断                    |
| INFO              | 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作 |
| WARNING           | 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的 |
| ERROR             | 由于一个更严重的问题导致某些功能不能正常运行时记录的信息     |
| CRITICAL          | 当发生严重错误，导致应用程序不能继续运行时记录的信息         |

- 该列表中的日志等级是从上到下依次增高，日志内容依次减少，即DEBUG可以显示所有日志，CRITICAL只能显示自己。例子如下：

```python
import logging

logging.debug("debug_msg")
logging.info("info_msg")
logging.warning("warning_msg")
logging.error("error_msg")
logging.critical("critical_msg")
```

输出结果

```zsh
WARNING:root:warning_msg
ERROR:root:error_msg
CRITICAL:root:critical_msg
```

说明默认的日志级别为WARNING

# logging的使用方法

## 常用函数

| 函数                                   | 说明                                 |
| :------------------------------------- | :----------------------------------- |
| logging.debug(msg, *args, **kwargs)    | 创建一条严重级别为DEBUG的日志记录    |
| logging.info(msg, *args, **kwargs)     | 创建一条严重级别为INFO的日志记录     |
| logging.warning(msg, *args, **kwargs)  | 创建一条严重级别为WARNING的日志记录  |
| logging.error(msg, *args, **kwargs)    | 创建一条严重级别为ERROR的日志记录    |
| logging.critical(msg, *args, **kwargs) | 创建一条严重级别为CRITICAL的日志记录 |
| logging.log(level, *args, **kwargs)    | 创建一条严重级别为level的日志记录    |
| logging.basicConfig(**kwargs)          | 对root logger进行一次性配置          |

> 不推荐使用basicConfig对日志等级进行自我创作，因为会影响代码的移植性，代码在别人那里容易起冲突

## 使用方法

日志输出方法

```python
logging.basicConfig(level=logging.DEBUG)#将日志的输出级别调节为debug
logging.basicConfig(filename='demo.log',level=logging.DEBUG)#将日志的输出到demo.log文件中
logging.basicConfig(filename='demo.log',filemote='w',level=logging.DEBUG)#先清空再写入，也可以设置为继续写
```

常用的输出（字符串格式化输出）[[3\]](https://www.cnblogs.com/kangsf2017/p/14700833.html#fn3)

```python
logging.debug("姓名 %s, 年龄%d",name,age)
logging.debug("姓名 %s, 年龄%d",% (name,age))
logging.debug("姓名 {}, 年龄{}".format(name,age))
logging.debug(f"姓名{name}, 年龄{age}")
```

```zsh
logging.basicConfig(format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",level=logging.DEBUG)
>>> 2020-07-16 15:35:58|DEBUG16-3.py:13|姓名 张三，年龄 18
```

# logger的高级应用

## 相关组件

| 名称                                                         | 作用                                             |
| :----------------------------------------------------------- | :----------------------------------------------- |
| Loggers                                                      | 记录器，提供应用程序代码直接使用的接口           |
| Handlers                                                     | 处理器，将记录器产生的日志发送至目的地           |
| Filters                                                      | 过滤器，提供更好的粒度控制，决定哪些日志会被输出 |
| Formatters                                                   | 格式化器，设置日志内容的组成结构和消息字段       |
| [![img](https://img2020.cnblogs.com/blog/2362656/202104/2362656-20210425203112008-1213759784.png)](https://img2020.cnblogs.com/blog/2362656/202104/2362656-20210425203112008-1213759784.png) |                                                  |

### Handlers

它们将日志分发到不同的目的地。可以是文件、标准输出、邮件、或者通过 socke、htt等协议发送到任何地方
setFormatter():设置当前Handler对象使用的消息格式

- Streamhandler
  标准输出stout分发器



```python
sh = logging.StreamHandler(stream=None)
```

- Filehandler
  将日志保存到磁盘文件的处理器



```python
fh = logging.FileHandler(filename,mode='a',encoding=None,delay=False)
```

- BaseRotatingHandler
- Rotating Filehandler
  滚动的多日志输出，按照时间or其他方式去生成多个日志
- TimedRotatingfilehandler

- 以下的使用较少

  - Sockethandler
  - Dataaramhandler
  - Smtphandler
  - Sysloghandler
  - Nteventloghandler
  - Httphandler
  - WatchedFilehandler
  - Qutelehandler
  - Nullhandler

  ### Formatters格式

  | 属性        | 格式            | 描述                                                  |
  | :---------- | :-------------- | :---------------------------------------------------- |
  | asctime     | %(asctime)s     | 日志产生的时间，默认格式为msecs2003-07-0816:49:45,896 |
  | msecs       | %(msecs)d       | 日志生成时间的亳秒部分                                |
  | created     | %(created)f     | time.tme)生成的日志创建时间戳                         |
  | message     | %(message)s     | 具体的日志信息                                        |
  | filename    | %(filename)s    | 生成日志的程序名                                      |
  | name        | %(name)s        | 日志调用者                                            |
  | funcname    | %( funcname)s   | 调用日志的函数名                                      |
  | levelname   | %(levelname)s   | 日志级別( DEBUG,INFO, WARNING, 'ERRORCRITICAL)        |
  | levene      | %( leveling)s   | 日志级别对应的数值                                    |
  | lineno      | %(lineno)d      | 日志所针对的代码行号（如果可用的话）                  |
  | module      | %( module)s     | 生成日志的模块名                                      |
  | pathname    | %( pathname)s   | 生成日志的文件的完整路径                              |
  | process     | %( (process)d   | 生成日志的进程D（如果可用）                           |
  | processname | (processname)s  | 进程名（如果可用）                                    |
  | thread      | %(thread)d      | 生成日志的线程D（如果可用）                           |
  | threadname  | %( threadname)s | 线程名（如果可用)                                     |