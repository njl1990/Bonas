#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import hashlib


def get_chunck_name():
	filename = 'crt.py'
	return filename
	
def get_conn_info():

	conn_info=('192.168.99.1', 9032)
	return conn_info
	
while True:
	
	# 	port=44670	#default
	
	# ip,port=input("server ip & port: ").split()

#		conn_info=(ip, int(port))
	client = socket.socket()
	client.connect(get_conn_info())
	
	#welcome
	print("connected... ")
	cmd=input("cmd: ")
	
	if len(cmd) == 0: continue
	if cmd.startswith("get"):
		client.send(cmd.encode())
		print(" send cmd ", cmd.encode())
		server_response = client.recv(1024)
		print("接收大小:", server_response)	#接收大小

		'''
		file_total_size = int(server_response.decode()) #½«ÎÄ¼þ´óÐ¡int»¯¡£
		received_size = 0  #³õÊ¼»¯½ÓÊÕÊý¾Ý´óÐ¡£¬Îª0
		filename = cmd.split()[1]  #»ñÈ¡ÎÄ¼þÃû
		f = open(filename + ".new", "wb") #ÒÔ¶þ½øÖÆÐÎÊ½Ð´Èë
		m = hashlib.md5()  #Îªmd5×¼±¸
		while received_size != file_total_size:
			if file_total_size - received_size > 1024: # ÒªÊÕ²»Ö¹Ò»´Î 
				size = 1024 
			else: # ×îºóÒ»´ÎÁË£¬Ê£¶àÉÙÊÕ¶àÉÙ
				size = file_total_size - received_size
			print("last receive:", size) 
			data = client.recv(size) #dataÖ»ÐèÒªÊÇÒ»Ð¡¸öÄÚ´æ£¬´óÐ¡Îª1k¾ÍºÃ
			received_size += len(data)
			m.update(data) #²»¶Ï¸üÐÂmd5 
			f.write(data) #²»¶ÏÐ´Èë
			# print(file_total_size,received_size)
		else: 
			new_file_md5 = m.hexdigest() #»ñÈ¡Ê®Áù½øÖÆµÄmd5 
		print("file recv done", received_size, file_total_size) 
		f.close() 
		server_file_md5 = client.recv(1024) #½ÓÊÕmd5Öµ 
		print("server file md5:", server_file_md5) 
		print("client file md5:", new_file_md5) 
		'''		
		client.close()

	elif cmd.startswith("ls"):
		client.send(cmd.encode()) #·¢ËÍÃüÁî£¬ÐÎÊ½ get filename
		server_response = client.recv(1024) #½ÓÊÕÎÄ¼þ´óÐ¡ÐÅÏ¢
		print("servr response:", server_response)
	#break;