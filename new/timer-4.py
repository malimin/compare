'''
用python实现定时任务
2018年12月13日
作者：贺鑫  联系方式：hexin4986@163.com
所属公司：北京令才科技
'''  


import os
import time
import sys
import datetime
import logging  
import my_logging

"""
#定时器时间读取文本：D:/RPA/setting/date/timing.txt

"""

print(666666)

#昨天
# 用法 python XXX.py getYesterday
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    result = yesterday.strftime("%Y%m%d") 
    return result


#停止”开启期间流程“
def end_During_Startup():
	import subprocess
	CREATE_NO_WINDOW = 0x08000000
	subprocess.call("D:/RPA/programs/AutoHotkey/AutoHotkeyU64.exe D:/RPA/programs/Main_Flow_Control/bat/s.ahk", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /IM rpa.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM core.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM MWICBCUKeyUI.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	# subprocess.call("taskkill /F /IM ffmpeg.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM AutoHotkey*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM chrome*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM RpaExecutor.exe", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill  /F /IM ie*", creationflags=CREATE_NO_WINDOW)


#开启期间
def run_main():
	end_During_Startup()
	time.sleep(1)
	os.system(r'D:\RPA\programs\Main_Flow_Control\start_main.bat')
	

#格式：   ./time2.py 上午邮件 全天邮件 停止开启期间 开启期间 关闭期间
def timerFun (one_run,two_run):
	#一个while死循环 保证程序一直在运行
	while True:
		#获取系统时间
		now = time.localtime()
		#打印系统时间
		# print(now)
		#如果系统时间的时 分 秒  和  我们指定时间的时 分 秒  各个比较都相等的话就运行程序
		if now.tm_hour == one_run.tm_hour and now.tm_min == one_run.tm_min and now.tm_sec == one_run.tm_sec:
			yesterday = getYesterday()
			print("时间到，开始执行第一次。。。")
			with open("D:/RPA/setting/date.txt",'w',encoding='UTF-8-sig') as date_txt:
				date_txt.write(yesterday+"-"+yesterday)
			if os.path.exists("D:/RPA/codes/rpa_code/1_setting/transfer.txt"):
				os.remove("D:/RPA/codes/rpa_code/1_setting/transfer.txt")
			run_main()
			# 为避免一分钟执行多次，休眠一分钟
			time.sleep(2)

		elif now.tm_hour == two_run.tm_hour and now.tm_min == two_run.tm_min and now.tm_sec == two_run.tm_sec:
			print("时间到，开始执行第二次。。。")
			if os.path.exists("D:/RPA/setting/date.txt"):
				os.remove("D:/RPA/setting/date.txt")
			if os.path.exists("D:/RPA/codes/rpa_code/1_setting/transfer.txt"):
				os.remove("D:/RPA/codes/rpa_code/1_setting/transfer.txt")
			run_main()
			# 为避免一分钟执行多次，休眠一分钟
			time.sleep(2)


#调用函数  并  进行传参
if __name__ == '__main__':

	#定时器时间读取文本：D:\RPA\setting\datetiming.txt
	#时间
	with open('D:/RPA/setting/timing.txt','r',encoding='utf-8') as f:
		timing = f.read()
		timing = timing.split("-")
		one_timing = timing[0]
		two_timing = timing[1]
	print("******** 定时器启动 ********")
	one_run = time.strptime(one_timing,"%H:%M:%S")
	print("您设定的第一次执行时间为：",time.strftime("%H:%M:%S",one_run))

	two_run = time.strptime(two_timing,"%H:%M:%S")
	print("您设定的第二次执行时间为：",time.strftime("%H:%M:%S",two_run))
	print("运行中。。。")

	timerFun(one_run,two_run)














