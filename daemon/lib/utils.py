#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket 


def getHostIp():
	return socket.gethostbyname(socket.getfqdn(socket.gethostname()))