#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

# 显示文件信息
def printls(ls):
	count_in_line = 4
	i=0

	for filename in ls:
		if i<count_in_line:
			print(filename+'   ',end='')
		else:
			print('');
			i=0
	print('\n');
	return
