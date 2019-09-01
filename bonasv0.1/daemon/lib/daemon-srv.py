#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import socket 
import os
import time
import sys
import json
import math
import des


#import user lab
import utils
import log
import process
import bm

#inport user module
import ls
import node

def LoginCheck(login_message):
	name = "bowen" #temp
	role = 'USER'
	return name, role

def Login(clientInfo):	
	# get login message	
	print("Login permission check:", end='')
	login_message = conn.recv(1024)
	# Permission Check 
	name,role=LoginCheck(login_message.decode)	# login message check
	userInfo = bm.UserInfo(name,role,clientInfo)
	userInfo.Regist()
	# 工作路径
	return userInfo

if __name__=='__main__': 
	hostIp = utils.getHostIp()
	hostPort = 4040

	# 启动服务
	server = socket.socket()
	server.bind((hostIp,hostPort))
	server.listen()

	# 发布接入点
	node = NodeManager()
	node.node_login()


	# 交互显示IP和端口
	print("ip: "+hostIp+" port: "+str(hostPort))
	print("Bonas daemon server is running...")


	# 工作状态
	isConnected = False
	isLogin = False
	initFilePath = "E:/Project/"

	clientInfo=None
	loginUser=None	
	bash=""
	# 工作循环
	while True:
		try:
			# print("————————————————————————————————————————————————")
			conn, addr = server.accept()
			#检查登录状态
			if not isLogin:
				#检查连接
				print("Wait for client...")
				print("Connected form ",addr[0],' at port ',addr[1])
				clientInfo=bm.ClientInfo(addr[0],addr[1])
				loginUser = Login(clientInfo);	# 用户登录

				if loginUser is not None:
					log.debug('login successful')
					isLogin=True 		# set log flag
					loginUser.path = initFilePath
					bash = loginUser.bash
				continue
			print(bash+"~$ ", end='')
			data = conn.recv(1024)
			if not data:
				print(" ");
				continue
			# 指令检索与处理
			cmd_str = data.decode()
			print(cmd_str)	# echo remote cmd

			# exit 命令
			if cmd_str.startswith('exit'):
				conn.close()
				isConnected=False
				isLogin=False

			# ls 命令
			elif cmd_str.startswith('ls'):
				if cmd_str.strip() == 'ls':	
					pathName = loginUser.path;
				else:
					cmd,pathName = datas.decode().strip().split()
				# 执行 ls 指令

				## 获取文件系统描述
				ls_str = ls.getLsStr(pathName);
				log.debug(str(ls_str))
				#ls.lsShow(ls_str)
				
				ls_json = json.dumps(ls_str)

				#文件系统描述加密
				# Unimplement
				conn.send(ls_json.encode('utf-8')) # send ls info

			# cd 命令
			elif cmd_str.startswith("cd"):
				cmd,path = data.decode().split()
				if os.path.exists(loginUser.path+path+'/'):
					if not os.path.isfile(path):   #判断是否该文件名为文件

						'''
						此处涉及到路径名在Linux 和 Windows下不统一的问题
						后续考虑修复

						'''
						loginUser.path=loginUser.path+path+'/'
						clientPath = loginUser.path.replace(initFilePath,'./') #变更为相对路径
						print (os.path.normpath(loginUser.path))
						# 输出修正后的路径
						conn.send(clientPath.encode('utf-8')) # send ls info
						continue
				else:
					conn.send('path not exist!'.encode())
			
			# get 命令
			elif cmd_str.startswith("get"):
				cmd,fileNameStr = data.decode().split()
				filename=loginUser.path+fileNameStr
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
						conn.send("CMD#DONE".encode()) #send file size
						f.close()
						#conn.send(m.hexdigest().encode()) #send md5
					else:
						print('Error#405: target is not a file')
						conn.send('Error#405'.encode());	#not a file
				else:
					print('Error#404: file is not exist')
					conn.send('Error#404'.encode());	#file is not exist
			else :
				print('Error#403: unknow command')
				conn.send(('unknow command \''+cmd_str+'\'').encode()) #error

		except Exception as e:
			print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
			print('错误所在的行号：', e.__traceback__.tb_lineno)
			print('错误信息', e)
			conn.close()
			isConnected=False;
			isLogin=False;
	server.close()