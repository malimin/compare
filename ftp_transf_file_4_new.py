from ftplib import FTP
import time,tarfile,os
import sys
import logging
import my_logging


# 连接ftp
def ftpconnect(host,port, username, password):
    logging.info('开始连接ftp')
    try:
        ftp = FTP()
        # 打开调试级别2，显示详细信息
        # ftp.set_debuglevel(2)
        ftp.connect(host, port)
        ftp.login(username, password)
        return ftp
    except Exception as e:
        print('连接ftp失败：')
        logging.info('连接ftp失败：')
        print(e)
        logging.info(e)
        raise


# 从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    logging.info('开始执行本地数据上传ftp函数')
    bufsize = 1024
    fp = open(localpath, 'rb')
    response = ftp.storbinary('STOR ' + remotepath, fp = fp, blocksize= bufsize)
    # ftp.set_debuglevel(0)
    print(response)
    fp.close()


# 主函数，上传本地文件到ftp
def upload_file_to_ftp():
    '''
        主函数，上传本地文件到ftp

        :return: 1. 已存在   2. 传输成功   3. 传输失败
    '''
    logging.info('**********************开始执行ftp上传模块**********************')
    try:
        # 需上传的文件路径
        email_attach_path = "D:/RPA/codes/rpa_code/1_setting/email_data.txt"
        # ftp上传结果的反馈文件路径
        ftp_result_file_path = "D:/RPA/codes/rpa_code/1_setting/FTP_result.txt"

        # 读取需上传文件的路径和文件名
        with open(email_attach_path,"r",encoding = "UTF-8") as email_attach:
            email_attach_data = email_attach.read()
            upload_file_path = email_attach_data.split("@")[1] # 需上传文件的路径
            upload_file_name = upload_file_path.split("\\")[4] # 文件名
        logging.info('需上传文件的路径:' + upload_file_path)
        logging.info('文件名' + upload_file_name)

        #host,port, username, password
        ftp = ftpconnect("10.49.1.3", 21,"ztwyls", "ZT_wyls2020")

        # 设置FTP当前操作的路径
        ftp.cwd('/home/ztwyls/upload/')
        print("当前路径为:", ftp.pwd(), "\n===")

        # 返回一个文件名列表
        filename_list = ftp.nlst()
        print("上传前包含的文件为:", filename_list, "\n===", "\n===")

        # 判断准备上传的文件在ftp上是否已经存在
        if upload_file_name in filename_list:
            print('ftp已经存在准备上传的文件')
            with open(ftp_result_file_path,"w",encoding = "UTF-8") as f:
                f.write("已存在")
            logging.info('ftp已经存在准备上传的文件')
            return 0


        # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
        uploadfile(ftp, upload_file_name, upload_file_path)
        time.sleep(2)


        # 返回一个文件名列表
        filename_list = ftp.nlst()
        print("上传后包含的文件为:", filename_list, "\n===", "\n===")


        # 通过是否包含已上传的文件名，判断是否上传成功
        if upload_file_name in filename_list:
            with open(ftp_result_file_path,"w",encoding = "UTF-8") as f:
                f.write("传输成功")
                logging.info('第一次传输成功')
            print("传输成功\n")
        else:
            logging.info('第一次传输失败，开始第二次传输ftp')
            ftp.cwd('/home/ztwyls/upload/')
            print("当前路径为:", ftp.pwd(), "\n===")

            # 返回一个文件名列表
            filename_list = ftp.nlst()
            print("上传前包含的文件为:", filename_list, "\n===", "\n===")

            # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
            uploadfile(ftp, upload_file_name, upload_file_path)
            time.sleep(2)

            if upload_file_name in filename_list:
                with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","w",encoding = "UTF-8") as f:
                    f.write("传输成功")
                    logging.info('第二次传输成功')
                print("传输成功\n")
            else:
                with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","w",encoding = "UTF-8") as f:
                    f.write("传输失败")
                    logging.info('第二次传输失败')
                print("传输失败\n")

        ftp.close() #关闭ftp
        print("结束")
        time.sleep(2)
    except:
        try:
            ftp.close()
        except:
            print("Error:连接ftp失败")
            raise



# if __name__ == "__main__":
#     try:
#         # 读取需上传的文件路径
#         email_attach_path = "D:/RPA/codes/rpa_code/1_setting/email_data.txt"
#         with open(email_attach_path,"r",encoding = "UTF-8") as email_attach:
#             email_attach_data = email_attach.read()
#             upload_file_path = email_attach_data.split("@")[1]
#             upload_file_name = upload_file_path.split("\\")[4]
#
#         #host,port, username, password
#         ftp = ftpconnect("10.49.1.3", 21,"ztwyls", "ZT_wyls2020")
#
#         # 设置FTP当前操作的路径
#         ftp.cwd('/home/ztwyls/upload/')
#         print("当前路径为:", ftp.pwd(), "\n===")
#
#         # 返回一个文件名列表
#         filename_list = ftp.nlst()
#         print("上传前包含的文件为:", filename_list, "\n===", "\n===")
#
#         # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
#         uploadfile(ftp, upload_file_name, upload_file_path)
#
#         # 返回一个文件名列表
#         filename_list = ftp.nlst()
#         print("上传后包含的文件为:", filename_list, "\n===", "\n===")
#         if upload_file_name in filename_list:
#             with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","w",encoding = "UTF-8") as f:
#                 f.write("传输成功")
#             print("传输成功\n")
#         else:
#             ftp.cwd('/home/ztwyls/upload/')
#             print("当前路径为:", ftp.pwd(), "\n===")
#
#             # 返回一个文件名列表
#             filename_list = ftp.nlst()
#             print("上传前包含的文件为:", filename_list, "\n===", "\n===")
#
#             # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
#             uploadfile(ftp, upload_file_name, upload_file_path)
#
#             if upload_file_name in filename_list:
#                 with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","w",encoding = "UTF-8") as f:
#                     f.write("传输成功")
#                 print("传输成功\n")
#             else:
#                 with open("C:/Users/Lenovo/Desktop/new_G6/1_setting/FTP_result.txt","w",encoding = "UTF-8") as f:
#                     f.write("传输成功")
#                 print("传输失败\n")
#
#         ftp.close() #关闭ftp
#         print("结束")
#         time.sleep(2)
#     except:
#         try:
#             ftp.close()
#         except:
#             pass
#             raise
#             print("Error:连接ftp失败")
#             time.sleep(2)