# --coding:utf-8 --

import logging

#用字典保存日志级别
format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}


# 开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, logname, loglevel, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

# 调用日志方法：
#     logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
#     logger.info(msg=u'参数是(%s)'% a)

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# # 创建一个logger
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.DEBUG)
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # 定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 给logger添加handler
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 记录一条日志
# logger.info('foorbar')
