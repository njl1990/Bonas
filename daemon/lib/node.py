
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import receivemail
import sendmail
import socket
import json
import array

class NodeManager(object):
	def __init__(self,host='',node_list=None):
		self.host = host
		self.node_list =node_list

	def node_login(self):
    	# 节点登入
    	# 获取当前在线节点；同时发布自身接入点
    	# 发布本节点接入
		list_data = self.add_node(receivemail.get_host_status())
		json_list = json.dumps(list(list_data))
		sendmail.update_host_status(json_list)

	def node_logout(self):
    	# 节点登出
    	# 获取当前在线的节点；同时删除自身接入点
    	# 发布本节点接入点
		list_data = self.remove_node(receivemail.get_host_status())
		if list_data is not None:
			json_list = json.dumps(list(list_data))
			sendmail.update_host_status(json_list)

	def add_node(self,list_data):
		for item in list_data:
			if item.find(socket.gethostname())>=0:
				return list_data
		add_item = socket.gethostname()+"@"+get_natapp_url()
		list_data.append(add_item)
		return list_data

	def remove_node(self,list_data):
		i = 0 ;
		remvoed_list = []

		for item in list_data:
			if item.find(socket.gethostname())<0:
				remvoed_list.append(item)
			i=i+1
		#print(remvoed_list)
		return remvoed_list

# 获取对外地址
def get_natapp_url():
	filename = '../exec/natapplog'
	#获取本地日志文件
	f = open(filename,"rb")
	patten = 'tcp://server.natappfree.cc'
	for l in f:
		line_str =  str(l)
		if  line_str.find(patten) > 0:
			f.close()
			result = line_str[line_str.find(patten):-3]
			return result
	f.close()
	return ""

if __name__ == "__main__":
	node = NodeManager()
	node.node_login()
	node.node_logout()
