#-*- coding:utf-8 -*-
# Create by MaLimin
# Create on 2020/4/29

import sys

class WrongParam(Exception):
    # print('参数错误')
    pass

def doomed():
    raise WrongParam()

print('参数：'+ str(len(sys.argv)))
try:
    if len(sys.argv) == 2:
        print('需要终止')
        doomed()
except WrongParam:
    raise
    print('aa')
print('正常结束')