#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import hashlib
import os
import json
import getpass
import des

#import user lab
import process
import gui

def get_chunck_name():
	filename = 'crt.py'
	return filename
	
def get_conn_info():
	ip,port=input("server ip & port: ").split()
	conn_info=(ip, int(port))
	#conn_info=('192.168.99.1', 9032)
	return conn_info


def get_user_info(conn_info):	
	
	#user="bowen"
	#pswd="1234"
	
	user = input("User:")
	pswd = getpass.getpass()
	loginfo = user+'@'+pswd

	client.send(loginfo.encode()) 
	bashStr = user + '@'+str(conn_info[0])+':'+str(conn_info[1])+'~$ '
	return bashStr

if __name__=='__main__': 

	conn_info=get_conn_info()
	client = socket.socket()
	client.connect(conn_info)

	# welcome
	bashStr=get_user_info(conn_info)


	while True:
		client = socket.socket()
		client.connect(conn_info)
		cmd=input(bashStr)

		# cmd		
		if len(cmd) == 0: continue
		
		# get
		if cmd.startswith("get"):

			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			if server_response.decode().startswith('Error'):
				print(server_response.decode())
				continue
			# get file size
			file_total_size = int(server_response.decode())
			print("File size:", server_response) 

			# receive file
			client.send(b"ready to recv file") 
			received_size = 0  
			filename = cmd.split()[1]
			if  os.path.exists(filename):
				filename=filename+'-copy'
			f = open(filename, "wb") 
			process_bar = process.ShowProcess(file_total_size, 'DONE')

			while received_size != file_total_size:
				if file_total_size - received_size > 4096: 
					size = 4096 
				else: 
					size = file_total_size - received_size
				data = client.recv(size)
				received_size += len(data)
				process_bar.show_process(received_size)
				f.write(data) 

			# receive	
			server_response = client.recv(1024)
			f.close() 
		# ls	
		elif cmd.startswith("ls"):
			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			lsjson=server_response.decode('utf-8')
			list = json.loads(lsjson)
			gui.printls(list)
			#print(server_response.decode('utf-8'))
		elif cmd.startswith("exit"):
			client.send(cmd.encode()) 
			client.close()
			break
		else :
			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			print(server_response.decode('utf-8'))
		#break;