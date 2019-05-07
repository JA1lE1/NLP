# -*-coding =utf-8-*-
'''
这是用于测试程序加载完毕后的提醒及python-moduel-logging的使用


'''

'''
yagmail 实现python邮件的发送
''' 
# import yagmail
	
	
# # yagmail.register('xxxxxx', 'xxxxxxx')  ## 这个要提前设置好

	
# yag = yagmail.SMTP('zlbnoj@163.com', host='smtp.163.com', port='465')

# yag.send('812126839@qq.com', '邮件主题', '这是邮件内容')

'''
logging的 使用
'''

'''
例1
'''
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')

'''
例2
'''

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
