#-*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/4/29

import os
import glob

# os.system('python C:\\Users\\10521\\Desktop\\compare\\test2.py 11')

# file =  open(r'C:\Users\10521\Desktop\compare\网银明细-20191130-1-01.txt', 'r', encoding='UTF-8-sig')
# for line in file:
#     line = line.strip('\n')
#     print(line)
#
# file.close()

# wait_upload_all_file = glob.glob('./*.txt')
# for file in path:
#     if
# print(wait_upload_all_file)
# print(len(wait_upload_all_file))
#
# # 如果1：待上传文件夹内【存在】txt文件
# if len(wait_upload_all_file) > 0:
#     with open('./aaa.txt', 'w', encoding='utf-8') as up_ftp_file:
#         for file in wait_upload_all_file:
#             with open('./' + file, 'r', encoding='utf-8') as wait_upload_file:
#                 up_ftp_file.write(wait_upload_file.read())
# # 如果2：待上传文件夹内【不存在】txt文件，上传文件内写入空
# else:
#     text = ''
#     with open('./aaa.txt', 'w', encoding='utf-8') as up_ftp_file:
#         up_ftp_file.write(text)

import time
from reprint import outprint

i = 100

for m in range(i):
    print(str(m) + '\r')
    time.sleep(1)