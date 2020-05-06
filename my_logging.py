# 方式1：原方式（暂时没有解决文本编码的问题）
import logging
import warnings
import time
import os

log_path = "D:\\RPA\\programs\\Main_Flow_Control\\log\\"
# print(log_path)
if not os.path.exists(log_path):
    # print('文件夹不存在')
    try:
        os.mkdir(log_path)
    except:
        raise
        # pass
else:
    # print('文件夹存在')
    pass


local_time = time.localtime(time.time())
nian = time.strftime('%Y',local_time)
yue = time.strftime('%m',local_time)
ri = time.strftime('%d',local_time)
shi = time.strftime('%H',local_time)
fen = time.strftime('%M',local_time)
miao = time.strftime('%S',local_time)

# warnings.filterwarnings('ignore')

# # 开启日志
# logging.basicConfig(level=logging.DEBUG,  
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
#                     datefmt='%Y-%m-%d %A %H:%M:%S',  
#                     filename="./log/"+nian+"_"+yue+"_"+'py_info_log.txt',
#                     filemode='a')
# logging.info("--step1--开启日志")

###################################################################

# 方式2
# import logging,os

# warnings.filterwarnings('ignore')

log_dir = 'D:\\RPA\\programs\\Main_Flow_Control\\log\\'+nian+yue+ri+'-record.txt'
def get_logger():
    fh = logging.FileHandler(log_dir,encoding='utf-8',mode="a") #创建一个文件流并设置编码utf8
    logger = logging.getLogger() #获得一个logger对象，默认是root
    logger.setLevel(logging.INFO)  #设置最低等级debug
    fm = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s： %(message)s",datefmt='%Y-%m-%d %A %H:%M:%S')  #设置日志格式
    
    logger.addHandler(fh) #把文件流添加进来，流向写入到文件
    fh.setFormatter(fm) #把文件流添加写入格式
    return logger
get_logger()
# logging.info("ok--测试")
# logging.info("--step1--开启日志")
