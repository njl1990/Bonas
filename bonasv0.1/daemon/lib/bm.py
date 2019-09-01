#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ClientInfo(): 
	clientIp =""
	clientPort = 0

	def __init__(self, clientIp="", clientPort=0): 
		self.clientIp = clientIp
		self.clientPort = clientPort
	

class UserInfo(): 
	client = None
	userName = ""
	role = ""
	bash = ""

	def __init__(self, userName="", role='GUEST',clientinfo=None): 
		self.userName = userName
		self.role = role
		self.client = clientinfo

	def Regist(self):
		print(self.userName+" as a "+ self.role)
		self.bash=self.userName+"@"+self.client.clientIp+":"+str(self.client.clientPort)