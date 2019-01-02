#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import socket 
import os
import time
import sys
import json
import math

#import user lab
import utils
import log
import process

#inport user module
import ls

def LoginCheck():
	loginName = "bowen" #temp
	return loginName



if __name__=='__main__': 
	hostIp = utils.getHostIp()
	hostPort = 9032

	# 启动服务
	server = socket.socket()
	server.bind((hostIp,hostPort))
	server.listen()



	# 交互显示IP和端口
	print("ip: "+hostIp+" port: "+str(hostPort))
	print("Bonas daemon server is running...")

	UserinfoStr=""

	# 工作循环
	while True:
		try:
			print("————————————")
			conn, addr = server.accept()
			
			#首次连接登录
			if UserinfoStr is "":
				print("Connected form ",addr[0],' at port ',addr[1])
				# Permission Check 
				print("Login:", end='')
				LoginUser=LoginCheck()	# login user
				print(LoginUser)
				UserinfoStr=LoginUser+"@"+hostIp+":"+str(addr[1])

				# 工作路径
				initFilePath = "E:/Project/"
				filePath=initFilePath
			
			print(UserinfoStr+"~$ ", end='')
			
			while 1:
				data = conn.recv(1024)
				if not data:
					break 
				# 指令检索与处理
				cmd_str = data.decode()
				print(cmd_str)	# echo remote cmd

				# exit 命令
				if cmd_str.startswith('exit'):
					filePath=initFilePath
					conn.send("bye".encode('utf-8')) # send ls info
					UserinfoStr=""

				# ls 命令
				elif cmd_str.startswith('ls'):
					if cmd_str == 'ls':	
						pathName = filePath;
					else:
						cmd,pathName = data.decode().split()
					# 执行 ls 指令

					## 获取文件系统描述
					ls_str = ls.getLsStr(pathName);
					log.debug(ls_str)
					#ls.lsShow(ls_str)
					
					ls_json = json.dumps(ls_str)

					#文件系统描述加密
					# Unimplement
					conn.send(ls_json.encode('utf-8')) # send ls info
				# cd 命令
				elif cmd_str.startswith("cd"):
					cmd,path = data.decode().split()
					if os.path.exists(filePath+path+'/'):
						if not os.path.isfile(path):   #判断是否该文件名为文件

							'''
							此处涉及到路径名在Linux 和 Windows下不统一的问题
							后续考虑修复

							'''
							filePath=filePath+path+'/'
							clientPath = filePath.replace(initFilePath,'./') #变更为相对路径
							print (os.path.normpath(filePath))
							# 输出修正后的路径
							conn.send(os.path.normpath(clientPath).encode('utf-8')) # send ls info
							break
					else:
						conn.send('path not exist!'.encode())
				# get 命令
				elif cmd_str.startswith("get"):
					cmd,fileNameStr = data.decode().split()
					filename=filePath+fileNameStr
					# log.debug('filename = '+filename)
					if os.path.exists(filename):
						if os.path.isfile(filename):   #判断是否该文件名为文件
							f = open(filename,"rb")
							file_size = os.stat(filename).st_size  #利用os.stat获取文件的大小

							# 发送文件大小
							conn.send(str(file_size).encode() ) #send file size
							conn.recv(1024) #等待确认，同时可以防止粘包。
							# log.debug('size:'+str(file_size))
							#计算发送次数

							process_bar = process.ShowProcess(file_size, 'DONE')
							# 发送文件 
							for l in f:
								conn.send(l)  #不断发送数据
								process_bar.show_process(f.tell())
							conn.send("done".encode()) #send file size
							f.close()
							#conn.send(m.hexdigest().encode()) #send md5
					else:
						conn.send('file is not exist.')
				else :
					conn.send(('unknow command \''+cmd_str+'\'').encode()) #error
		except:
			print('Error')
			print(sys.exc_info())
			continue
		else:
			continue
	server.close()