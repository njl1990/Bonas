#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import hashlib


def get_chunck_name():
	filename = 'crt.py'
	return filename
	
def get_conn_info():
	#ip,port=input("server ip & port: ").split()
	#conn_info=(ip, int(port))
	conn_info=('192.168.99.1', 9032)
	return conn_info


if __name__=='__main__': 
	while True:
		client = socket.socket()
		client.connect(get_conn_info())

		#welcome
		print("connected... ")
		cmd=input("cmd: ")
		
		if len(cmd) == 0: continue
		if cmd.startswith("get"):
			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			print("servr response:", server_response)
			client.send(b"ready to recv file") 
			file_total_size = int(server_response.decode()) 
			received_size = 0  
			filename = cmd.split()[1] 
			f = open(filename + ".new", "wb") 

			while received_size != file_total_size:
				if file_total_size - received_size > 4096: 
					size = 4096 
				else: 
					size = file_total_size - received_size
				print("last receive:", size) 
				data = client.recv(size)
				received_size += len(data)
				f.write(data) 
				# print(file_total_size,received_size)

			server_response = client.recv(1024)
			print("servr response:", server_response)

			print("file recv done", received_size, file_total_size) 
			f.close() 
			client.close()


		elif cmd.startswith("ls"):
			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			print("servr response:", server_response.decode('utf-8'))

		else :
			client.send(cmd.encode()) 
			server_response = client.recv(1024)
			print("servr response:", server_response.decode('utf-8'))
		#break;