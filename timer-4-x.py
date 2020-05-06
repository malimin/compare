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
	subprocess.call("taskkill /IM rpa.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM core.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM AutoHotkey*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM chrome*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM RpaExecutor.exe", creationflags=CREATE_NO_WINDOW)


#开启期间
def run_main(run_bat_path,number):
	end_During_Startup()
	time.sleep(1)
	run = run_bat_path + " " + str(number)
	print(run)
	os.system(run)
	# subprocess.call("python D:/RPA/programs/Main_Flow_Control/G6Crreg.py %s" % date_between,
	# 				creationflags=CREATE_NO_WINDOW,
	# 				)

#删除日期文件
def remove_date():
	if os.path.exists("D:/RPA/setting/date.txt"):
		os.remove("D:/RPA/setting/date.txt")
	if os.path.exists("D:/RPA/codes/rpa_code/1_setting/date.txt"):
		os.remove("D:/RPA/codes/rpa_code/1_setting/date.txt")

#格式：   ./time2.py 上午邮件 全天邮件 停止开启期间 开启期间 关闭期间
def timerFun (one_run, two_run, three_run):
	#一个while死循环 保证程序一直在运行
	while True:
		#获取系统时间
		now = time.localtime()
		#打印系统时间
		# print(now)
		#如果系统时间的时 分 秒  和  我们指定时间的时 分 秒  各个比较都相等的话就运行程序
		if now.tm_hour == one_run.tm_hour and now.tm_min == one_run.tm_min and now.tm_sec == one_run.tm_sec:
			remove_date()
			yesterday = getYesterday()
			print("时间到，开始执行第一次。。。")
			with open("D:/RPA/setting/date.txt",'w',encoding='UTF-8-sig') as date_txt:
				date_txt.write(yesterday+"-"+yesterday)

			run_bat_path = "D:/RPA/programs/Main_Flow_Control/start_main.bat"
			number = 1
			run_main(number)
			# 为避免一分钟执行多次，休眠一分钟
			time.sleep(2)

		elif now.tm_hour == two_run.tm_hour and now.tm_min == two_run.tm_min and now.tm_sec == two_run.tm_sec:
			print("时间到，开始执行第二次。。。")
			remove_date()
			run_bat_path = "D:/RPA/programs/Main_Flow_Control/start_main.bat"
			number = 2
			run_main(number)
			# 为避免一分钟执行多次，休眠一分钟
			time.sleep(2)

		elif now.tm_hour == three_run.tm_hour and now.tm_min == three_run.tm_min and now.tm_sec == three_run.tm_sec:
			print("时间到，开始执行第三次。。。")
			remove_date()
			yesterday = getYesterday()
			try :
				Todaydate = time.strftime("%Y-%m-%d", time.localtime())
				with open("D:/RPA/setting/date.txt",'w',encoding='UTF-8-sig') as date_txt:
					date_txt.write(yesterday+"-"+yesterday)
				if os.path.exists("D:/RPA/record/%s/第1次执行结果统计.txt"%(Todaydate)):

					with open("D:/RPA/record/%s/第1次执行结果统计.txt"%(Todaydate),'r',encoding='UTF-8-sig') as f:
						k  = f.read()
						print("D:/RPA/record/%s/第1次执行结果统计.txt"%(Todaydate))
						print(k)
						if "失败" in k :
							print("111111111111111")
							run_bat_path = "C:/Users/Lenovo/Desktop/new_G6/Main_Flow_Control/start_main_3.bat"
							number = 3
							run_main(run_bat_path, number)
						else:
							pass

							# import subprocess
							# CREATE_NO_WINDOW = 0x08000000
							# # 无失败任务，发送邮件反馈人工无失败记录
							# subprocess.call("D:/RPA/programs/RPA154/RpaExecutor/RpaExecutor.exe --file=D:/RPA/codes/rpa_code/1_email/email.rpafile",
							# 				# creationflags=CREATE_NO_WINDOW,
							# 				)
			except FileNotFoundError:
				print("未找到第一次执行结果")
			# 	remove_date()
			# 	print("时间到，开始执行第一次。。。")
			# 	with open("D:/RPA/setting/date.txt",'w',encoding='UTF-8-sig') as date_txt:
			# 		date_txt.write(yesterday+"-"+yesterday)

			# 	run_bat_path = "D:/RPA/programs/Main_Flow_Control/start_main.bat"
			# 	number = 1
			# 	run_main(number)
			# 	# 为避免一分钟执行多次，休眠一分钟
			# 	time.sleep(2)

			# # 为避免一分钟执行多次，休眠一分钟
			# time.sleep(2)


#调用函数  并  进行传参
if __name__ == '__main__':
	#定时器时间读取文本：D:\RPA\setting\datetiming.txt
	#时间
	with open('D:/RPA/setting/timing.txt','r',encoding='utf-8') as f:
		timing = f.read()
		timing = timing.split("-")
		one_timing = timing[0]
		two_timing = timing[1]
		three_timing = timing[2]
	print("******** 定时器启动 ********")
	one_run = time.strptime(one_timing,"%H:%M:%S")
	print("您设定的第一次执行时间为：",time.strftime("%H:%M:%S",one_run))

	two_run = time.strptime(two_timing,"%H:%M:%S")
	print("您设定的第二次执行时间为：",time.strftime("%H:%M:%S",two_run))

	three_run = time.strptime(three_timing,"%H:%M:%S")
	print("您设定的第二次执行时间为：",time.strftime("%H:%M:%S",three_run))
	print("运行中。。。")

	timerFun(one_run, two_run, three_run)



