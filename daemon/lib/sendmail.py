
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr



def send_email(from_addr, to_addr, subject, content,password):
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.163.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())

def sendml(topic,content):
	send_email(u"m18566506320@163.com",u"m18566506320@163.com",topic,content,u"bonasNanbowen123")
	
	
def update_host_status(content):
	sendml('Bonas Client List',content)
	
if __name__ == "__main__":
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    update_host_status("[\"TEST@tcp://server.natappfree.cc:43623\"]")