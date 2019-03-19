#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import uuid
from urllib import parse,request

def get_mac_address(): 
	mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
	return ":".join([mac[e:e+2] for e in range(0,11,2)])


server_port_str=sys.argv[1]
host_port_str=sys.argv[2]
device_id = get_mac_address()


textmod={'device_id':device_id,'address':host_port_str}
textmod = parse.urlencode(textmod)

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url='http://'+server_port_str+'/ci/dlgin/'
req = request.Request(url='%s%s%s' % (url,'?',textmod),headers=header_dict)
res = request.urlopen(req)
res = res.read()
print('response:' + res.decode(encoding='utf-8'))
#输出内容:登录成功

