
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import poplib,json,socket
from poplib import POP3
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def get_host_status():
	p = POP3('pop.163.com')
	p.user('m18566506320@163.com')
	p.pass_('bonasNanbowen123')
	#获取邮件清单
	mail_num,size=p.stat()
	i=1
	content=""
	while i<=mail_num:
		resp, lines, octets = p.retr(i)
		# lines存储了邮件的原始文本的每一行,
		# 可以获得整个邮件的原始文本:
		msg_content = b'\r\n'.join(lines).decode('utf-8')
		# 解析出邮件:
		msg = Parser().parsestr(msg_content)
		#print(msg)
		topic = msg.get('Subject', '')
		if topic == 'Bonas Client List':
			# 是清单信息邮件
			content=msg.get_payload(decode=True).decode('utf-8')
			p.dele(i)
		else:
			a=1
			p.dele(i)
		i=i+1
		p.quit()

	# 获取当前在线节点；同时发布自身接入点
	if content != "" :
		node_array =json.loads(content)
		#print("exist")
		return list(node_array)

	array = [socket.gethostname()+"@"+get_natapp_url()]
	return array


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
	list =get_host_status()
	print(list)