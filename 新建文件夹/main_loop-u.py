# usr/bin/python
# -*- coding: UTF-8-sig -*-
import time 
import datetime
import sys
import os
import logging  
import warnings
import subprocess
# from datetime import datetime
import xlwings as xw
import time
import sys
import shutil
import datetime
import glob
"""
	任务命令文件：			D:/RPA/basic_data/all_data/当前待执行信息.txt
	网盾银行基础信息表：		D:/RPA/basic_data/all_data/网盾银行基础信息表.xlsx
	成功返回文件：			D:/RPA/programs/Main_Flow_Control/finish.txt
	对比时间文件：			D:/RPA/codes/rpa_code/1_setting/run_time.txt
	中转文件：				D:/RPA/codes/rpa_code/1_setting/transfer.txt
	bat路径：				D:/RPA/programs/Main_Flow_Control
	rpa开始状态文本 ： 		D:/RPA/setting/date/status_code.txt
	bat文件命名格式    		定时文本    二次任务做完后上传总记录文件格式/内容
	执行日期文件 ：			D:/RPA/codes/rpa_code/1_setting/date.txt
	
	用户维护路径：
		定时文件：	D:/RPA/setting/timing.txt
		格式：		16:59:10-17:01:30
		数据区间：	D:/RPA/setting/data.txt
		格式：		20191107-20191112
"""




#读取基础数据-------------------------------------------------------------------------------
#接收的文件号file_num
file_num = sys.argv[1]
path= r'D:\RPA\basic_data\all_data\网盾银行基础信息表.xlsx'
bat_path = r"D:\RPA\programs\Main_Flow_Control\bat\start.bat"
# 定义要创建的目录
localtime = time.strftime("%Y-%m-%d", time.localtime())
mkpath="D:/RPA/record/"+localtime

#创建当日上传文件夹
def mkdir(path):
	# 去除首位空格
	path=path.strip()
	# 去除尾部 \ 符号
	path=path.rstrip("\\")
	isExists=os.path.exists(path)
	# 判断结果
	if not isExists:
		# 如果不存在则创建目录
		# 创建目录操作函数
		os.makedirs(path) 
	else:
		# 如果目录存在则不创建，并提示目录已存在
		pass
# 调用函数
mkdir(mkpath)

#判断文件夹下是否包含后缀名为。txt的文件，包含几个
def if_file(Dir):
	if not os.path.exists(Dir):
		os.makedirs(Dir)
	Files=os.listdir(Dir)
	for k in range(len(Files)):
		# 提取文件夹内所有文件的后缀
		Files[k]=os.path.splitext(Files[k])[1]
	# 文件的后缀
	Str='.txt'
	num = 0
	for file_num in Files:
		if Str == file_num:
			num += 1
			print(999)
		else:
			pass
	return num

#传输定义编号，计算时间总数
def transfer_define_num(time_str):
	time_arr = time_str.split('-',2)
	time_number =  int(time_arr[0])*3600+int(time_arr[1])*60+int(time_arr[2])
	return time_number

#读取任务列表
def read_data(path):
	# 导入xlwings模块，打开Excel程序，默认设置：程序可见，只打开不新建工作薄，屏幕更新关闭
	appRead = xw.App(visible=False,add_book=False)
	#打开工作簿
	wbRead=appRead.books.open(path)
	#引用sheet
	shtRead = wbRead.sheets[0]
	#获取a,b,2列的值放入列表
	rng = shtRead.range('a1').expand('table')
	nrows = rng.rows.count
	a=''
	a = shtRead.range(f'a1:m{nrows}').value
	#将第一列作为key第二列作为值传入字典
	for_list = []
	# Dict = CIMultiDict()
	for line in a:
		for_list.append(line)
		if "G6" in line:
			break
	# print(for_list)		
	wbRead.close()
	appRead.quit()
	return for_list

#创建空文档
def Create_empty_document():
	Dir = 'D:/RPA/summary_data/' + date_between
	my_endtime = date_between.split("_")
	num = file_num
	if num < 10:
		num1 = "0" + str(num)
	path = 'D:/RPA/summary_data/%s/网银明细-%s-%s-%s.txt'%(date_between,my_endtime[1],1,num1)
	txt = ''
	# 写入文档
	with open(path,'w',encoding='utf-8') as f:
		f.write(txt)
	return path

#杀掉所有rpa相关进程
def end_During_Startup():
	import subprocess
	CREATE_NO_WINDOW = 0x08000000
	subprocess.call("D:/RPA/programs/AutoHotkey/AutoHotkeyU64.exe D:/RPA/programs/Main_Flow_Control/bat/s.ahk", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /IM rpa.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM core.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM ffmpeg.exe", creationflags=CREATE_NO_WINDOW,shell=True)
	subprocess.call("taskkill /F /IM AutoHotkey*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM chrome*", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill /F /IM RpaExecutor.exe", creationflags=CREATE_NO_WINDOW)
	subprocess.call("taskkill  /F /IM ie*", creationflags=CREATE_NO_WINDOW)
	
	# subprocess.call("taskkill  /F /IM BOCUsertool*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM DBSvr_ABC*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM USBKeyTools*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM WDCertM_CCB*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM ISCertD_abchina*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM BOCBank*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM D4Svr_CCB*", creationflags=CREATE_NO_WINDOW)
	# subprocess.call("taskkill  /F /IM CCBCertificate*", creationflags=CREATE_NO_WINDOW)
	#将状态码文件改为0（未运行状态）
	with open('D:/RPA/setting/date/status_code.txt','w',encoding='UTF-8-sig') as status_code:
		status_code.write("0")

#启动bat
def run_bat(bat_path,up_file,bat_name):
	end_During_Startup()

	time.sleep(2)
	#拼接路径和bat名称，bat_name为传入bat的传参
	bat = bat_path + ' ' + bat_name
	os.system(bat)

	#判断成功文件是否存在，如果存在删除成功文件
	finish_file = os.path.exists("D:/RPA/programs/Main_Flow_Control/finish.txt")
	if finish_file is True:
		os.remove("D:/RPA/programs/Main_Flow_Control/finish.txt")
	autoGo(up_file)

#循环主流程函数
def autoGo(up_file):
	
	with open(up_file,'a',encoding='UTF-8-sig') as transfer:
		while True:
			time.sleep(10)
			print(1111)
			finish_file = os.path.exists("D:/RPA/programs/Main_Flow_Control/finish.txt")
			
			#如果finish文本存在，读取其中的内容拼接到中转文本中
			if finish_file is True:
				print(2222)
				#读取成功文本内容写入中转
				finish_path = open("D:/RPA/programs/Main_Flow_Control/finish.txt",'r',encoding='UTF-8-sig')
				finish_content = finish_path.read()
				finish_path.close()
				transfer.write(p+"$"+finish_content)
				transfer.write('\n')

				#如果finish_content包含 “*密码*” 字符将次条数据的密码追加到password_error中，
				#做下一条数据时首先判断密码单据密码是否在password_error列表中
				if "密码" in finish_content:
					password=p.split("@")[6]
					password_error.append(password)

				break
			else:
				print(3333)
				try:
					#状态码，开始为1，停止为0
					status_info0 = open("D:/RPA/setting/date/status_code.txt",'r',encoding='UTF-8-sig')
					status_info = status_info0.read()
					status_info0.close()
					#时间
					time_path = open("D:/RPA/codes/rpa_code/1_setting/run_time.txt",'r',encoding='UTF-8-sig')
					rpa_time = time_path.read()
					time_path.close()
					print(status_info)
					if  "1" in status_info:
						print("600")
						# logging.info("--step1.2.2--获取当前时间字符串")
						#获取当前时间戳
						current_timestamp = time.localtime()
						#格式化当前时间戳
						str_currenttime = time.strftime("%H-%M-%S", current_timestamp)
						#如果更新时间文本不存在
						if not(os.path.exists(rpa_time)):
							logging.info("--step1.2.2--time文件不存在")
						# 开始对比时间
						#获取当前时间总数
						rpa_compare_curr = transfer_define_num(str_currenttime)
						#获取rpa时间总数
						rpa_compare_txt  = transfer_define_num(rpa_time)
						print(rpa_compare_txt,rpa_compare_curr)

						if (rpa_compare_curr-rpa_compare_txt) > 600:
							end_During_Startup()
							#判断上次开的是哪一流程，重新开启
							transfer.write(p+"$失败")
							transfer.write('\n')
							break
				except:
					pass

# 获取今天的日期
def getToday():
	today=datetime.date.today()
	result = today.strftime("%Y%m%d")
	return result



#清空指定文件夹
def delfile(path):
    fileNames = glob.glob(path + r'\*') 
    for fileName in fileNames:
        try:
            os.remove( fileName)
        except:
            try:
                os.rmdir( fileName)
            except:
                delfile( fileName)
                os.rmdir( fileName)




# 开始循环--------------------------------------------------------------------------------------
print("开始主循环//////////////////////////")
#读取基础数据-------------------------------------------------------------------------------
path= r'D:\RPA\basic_data\all_data\网盾银行基础信息表.xlsx'
bat_path = r"D:\RPA\programs\Main_Flow_Control\bat\start.bat"
# 定义要创建的目录
localtime = time.strftime("%Y-%m-%d", time.localtime())
mkpath="D:/RPA/record/"+localtime
# 调用函数
mkdir(mkpath)

# 生成全部任务
run_task = read_data(path)
print(run_task)

# 初始化下载数据时间区间
user_date_file = "D:/RPA/setting/date.txt"
rpa_date_file = r"D:\RPA\codes\rpa_code\1_setting\date.txt"
if os.path.exists(rpa_date_file):
	os.remove(rpa_date_file)
if os.path.exists(user_date_file):
	shutil.copy(user_date_file, rpa_date_file)
	try:
		with open(user_date_file, "r", encoding='UTF-8-sig') as user_date:
			date = user_date.read()
			# print(date)
			date = date.split("-")
			start_date = date[0]
			end_date = date[1]
	except:
		raise
else:
	today = getToday()
	start_date = today
	end_date = today

#创建密码错误列表
password_error = []

# 第一次循环：循环基础数据表生成的任务
i = 0
for this_line in run_task:
	if i == 0:
		pass
	else:
		up_file = 'D:/RPA/codes/rpa_code/1_setting/transfer.txt'
		p = ""
		for this in this_line:
			if type(this) is float:
				this = str(int(this))
			p += str(this) + "@"
		print(p)

		#读取中转文本内容，准备判断其中是否包含当前数据
		if not os.path.exists('D:/RPA/codes/rpa_code/1_setting/transfer.txt'):
			with open('D:/RPA/codes/rpa_code/1_setting/transfer.txt','w',encoding='UTF-8-sig') as f:
				a = f.write("")
		with open('D:/RPA/codes/rpa_code/1_setting/transfer.txt','r',encoding='UTF-8-sig') as f:
			a = f.read()
		#判断中转文本中是否有当前任务的银行账号（断点续传）
		if this_line[3] in a:
			print("当前任务已做过，跳过，开始做下一任务")
		else:
			#判断当前任务密码是否在密码错误列表中，如果存在-跳过，如果不存在
			if this_line[6] in password_error:
				with open(up_file,'a',encoding='UTF-8-sig') as W_transfer:
					W_transfer.write(p+"$密码错误")
					W_transfer.write('\n')
			else:
				with open(r'D:\RPA\basic_data\all_data\当前待执行信息.txt','w',encoding='UTF-8-sig') as f:
					f.write(p)
				bat_name = this_line[6]
				run_bat(bat_path,up_file,bat_name)


		time.sleep(10)	
	i += 1



# 第二次循环：读取中转文件，提取出失败任务，重新执行--------------------------------------------------------------------------
time_path = open("D:/RPA/codes/rpa_code/1_setting/transfer.txt",'r',encoding='UTF-8-sig')
path = mkpath
num = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]) + 1
up_file = mkpath+'/第'+str(num)+'次执行结果统计.txt'

for line in time_path:
	line=line.strip('\n')
	if "失败" in line:
		print("-------"+line+"---------")
		line = line.strip("$失败")
		p = line
		line = line.split("@")

		#读取中转文本内容，准备判断其中是否包含当前数据
		a = ""
		try:
			with open(up_file,'r',encoding='UTF-8-sig') as f:
				a = f.read()
		except FileNotFoundError:
			a = [0,1]
		#判断中转文本中是否有当前任务的银行账号（断点续传）
		if line[3] in a:
			print("当前任务已做过，跳过，开始做下一任务")
		else:
			with open('D:/RPA/basic_data/all_data/当前待执行信息.txt','w',encoding='UTF-8-sig') as f:
				f.write(p)
			bat_name = line[6]
			print("-----"+bat_name+"--------")
			run_bat(bat_path,up_file,bat_name)
	else:
		with open(up_file,'a',encoding='UTF-8-sig') as f:
			f.write(line)
			f.write('\n')
time_path.close()


# #判断是否失败，如果失败不做数据处理，生成空的上传文本
# date_between = start_date + "_" + end_date
# with open(up_file,'r',encoding='UTF-8-sig') as f:
# 	result = f.read()
# if "失败" in result:#
# 	#创建空文档
# 	path = Create_empty_document()
# 	#更新emaildata
# 	try:
# 		with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'w',encoding='UTF-8-sig') as f:
# 			a = f.write("-2@" + path)
# 	except FileNotFoundError:
# 		pass
# else:
	# 调用数据处理
	# 将开始时间和结束时间作为参数，传递给数据处理crreg
CREATE_NO_WINDOW = 0x08000000
subprocess.call("python D:\RPA\programs\Main_Flow_Control\G6Crreg.py %s" % date_between,
				creationflags=CREATE_NO_WINDOW,)
#判断表处理是否成功  / 银联处理多个表
with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'r',encoding='UTF-8-sig') as f:
	result = f.read().split("@")
	result_code,result_path = result[0],result[1]
	
if str(result_code) == "-1":
	#创建空文档
	path = Create_empty_document()
	#更新emaildata
	try:
		with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'w',encoding='UTF-8-sig') as f:
			a = f.write("-1@" + path)
	except FileNotFoundError:
		pass
else:
	#复制文件到待上传文件夹
	if not os.path.exists("C:/Users/Lenovo/Desktop/new_G6/wait_uploading"):
        os.makedirs("C:/Users/Lenovo/Desktop/new_G6/wait_uploading")
    shutil.copyfile(result[1],"C:/Users/Lenovo/Desktop/new_G6/wait_uploading")


time.sleep(2)


#判断文件号传参为1/2时上传ftp
# num = file_num
# Dir = 'D:/RPA/summary_data/' + date_between
# num = if_file(Dir)
#创建当日上传ftp文件夹
mkpath="C:/Users/Lenovo/Desktop/new_G6/up_ftp/" + localtime
mkdir(mkpath)
if num == 1 or num == 2:
	path = "C:/Users/Lenovo/Desktop/new_G6/wait_uploading"
	if os.path.exists(path):
		my_endtime = date_between.split("_")
		num = file_num
		if num < 10:
			num1 = "0" + str(num)
		Dir = 'C:/Users/Lenovo/Desktop/new_G6/up_ftp/%s/网银明细-%s-%s-%s.txt'%(date_between,my_endtime[1],1,num1)

		if len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]) > 0:
			with open(Dir,'w',encoding='UTF-8-sig') as Dir_f:
				for k in os.listdir(path):
					with open(path + "/" + k,'r',encoding='utf-8') as f:
						Dir_f.write(f.read()) 
		else:
			txt = ''
			# 写入文档
			with open(Dir,'w',encoding='utf-8') as f:
				f.write(txt)


	#更新emaildata
	#判断表处理是否成功
	with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'r',encoding='UTF-8-sig') as f:
		result = f.read().split("@")
		result_code,result_path = result[0],result[1]
		
	if str(result_code) == "-1" or str(result_code) == "-2":
		length = str(result_code)
	else:
		#有数据，计算数据总数
		with open(Dir,'r',encoding='UTF-8-sig') as f:
			text=f.read()
			length=len(text.splitlines())
	try:
		with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'w',encoding='UTF-8-sig') as f:
			a = f.write(length + "@" + Dir)
	except FileNotFoundError:
		pass
	
	# 上传ftp
	CREATE_NO_WINDOW = 0x08000000
	subprocess.call("python D:/RPA/programs/Main_Flow_Control/ftp_transf_file.py",
					creationflags=CREATE_NO_WINDOW,
					)

with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","r",encoding = "UTF-8") as f:
	FTP_result = f.read()
    if "成功" in FTP_result :
		#备份等待上传文件夹
		Todaydate = getToday()
		source_path = os.path.abspath('C:/Users/Lenovo/Desktop/new_G6/wait_uploading')
		target_path = os.path.abspath('C:/Users/Lenovo/Desktop/new_G6/up_ftp/' +  Todaydate)
		if not os.path.exists(target_path):
		    os.makedirs(target_path)
		if os.path.exists(source_path):
		    # root 所指的是当前正在遍历的这个文件夹的本身的地址
		    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
		    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
		    for root, dirs, files in os.walk(source_path):
		        for file in files:
		            src_file = os.path.join(root, file)
		            shutil.copy(src_file, target_path)
		            print(src_file)
		#清空等待上传文件夹
		path = r'C:\Users\Lenovo\Desktop\new_G6\wait_uploading'
		delfile(path)
		
    elif "失败" in FTP_result
	    with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'r',encoding='UTF-8-sig') as f:
			result = f.read().split("@")
			result_code,result_path = result[0],result[1]
    	with open("D:/RPA/codes/rpa_code/1_setting/email_data.txt",'w',encoding='UTF-8-sig') as f:
			a = f.write("-3@" + result[1])

#备份等待上传文件夹
Todaydate = getToday()
source_path = os.path.abspath('C:/Users/Lenovo/Desktop/new_G6/wait_uploading')
target_path = os.path.abspath('C:/Users/Lenovo/Desktop/new_G6/up_ftp/' +  Todaydate)
if not os.path.exists(target_path):
    os.makedirs(target_path)
if os.path.exists(source_path):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(source_path):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, target_path)
            print(src_file)
#清空等待上传文件夹
path = r'C:\Users\Lenovo\Desktop\new_G6\wait_uploading'
delfile(path)


# 发送邮件
#拼接路径和bat名称，bat_name为传入bat的传参
subprocess.call("D:/RPA/programs/RPA154/RpaExecutor/RpaExecutor.exe --file=D:/RPA/codes/rpa_code/1_email/email.rpafile",
				# creationflags=CREATE_NO_WINDOW,
				)
time.sleep(2)
#执行日期删除，否则第二次跑会执行*********
#判断成功文件是否存在，如果存在删除成功文件
if os.path.exists("D:/RPA/setting/date.txt"):
	os.remove("D:/RPA/setting/date.txt")
if os.path.exists("D:/RPA/codes/rpa_code/1_setting/date.txt"):
	os.remove("D:/RPA/codes/rpa_code/1_setting/date.txt")
if os.path.exists("D:/RPA/codes/rpa_code/1_setting/transfer.txt"):
	os.remove("D:/RPA/codes/rpa_code/1_setting/transfer.txt")







# 流程完毕清除所有程序
end_During_Startup()
print("运行完成。。。")
























































-------------------------------------------------------------------------------------------------------------------

# 将本次运行记录结果路径，记录到邮件附件2
email_path2 = "D:/RPA/codes/rpa_code/1_setting/email_data_record.txt"
with open(email_path2,'w',encoding='UTF-8-sig') as f:
	f.write(up_file)

# 调用数据处理
# 将开始时间和结束时间作为参数，传递给数据处理crreg
date_between = start_date + "_" + end_date
CREATE_NO_WINDOW = 0x08000000
subprocess.call("python D:/RPA/programs/Main_Flow_Control/crreg.py %s" % date_between,
				creationflags=CREATE_NO_WINDOW,
				)
time.sleep(2)

# 发送邮件
# bat_path1 = r"D:\RPA\programs\Main_Flow_Control\bat\email.bat"
# os.system(bat_path1)
subprocess.call("D:/RPA/programs/RPA154/RpaExecutor/RpaExecutor.exe --file=D:/RPA/codes/rpa_code/1_email/email.rpafile",
				# creationflags=CREATE_NO_WINDOW,
				)
time.sleep(2)


#执行日期删除，否则第二次跑会执行*********
#判断成功文件是否存在，如果存在删除成功文件
# finish_file = os.path.exists("D:/RPA/setting/date.txt")
# if finish_file is True:
# 	os.remove("D:/RPA/setting/date.txt")
# rpa_date_file = "D:/RPA/codes/rpa_code/1_setting/date.txt"
# if os.path.exists(rpa_date_file):
# 	os.remove(rpa_date_file)
if os.path.exists("D:/RPA/setting/date.txt"):
	os.remove("D:/RPA/setting/date.txt")
if os.path.exists("D:/RPA/codes/rpa_code/1_setting/date.txt"):
	os.remove("D:/RPA/codes/rpa_code/1_setting/date.txt")
if os.path.exists("D:/RPA/codes/rpa_code/1_setting/transfer.txt"):
	os.remove("D:/RPA/codes/rpa_code/1_setting/transfer.txt")

# 流程完毕清除所有程序
end_During_Startup()

print("运行完成。。。")

# #############保存为txt文本，上传txt到ftp##################

# savetxt_path_bat = "D:/RPA/programs/Main_Flow_Control/bat/savetxt.bat"
# os.system(savetxt_path_bat)

############################################################













