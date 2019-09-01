#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import sys

def getLsStr(filename):
	lsStr = all_path(filename)
	return lsStr

def lsShow(argv):
	for item in argv:
		print(item)

def all_path(dirname):

	result = []#所有的文件

	for maindir, subdir, file_name_list in os.walk(dirname):

		#print("1:",maindir) #当前主目录
		#print("2:",subdir) #当前主目录下的所有目录
		#print("3:",file_name_list)  #当前主目录下的所有文件
		
		for subdir_name in subdir:
			apath = "["+subdir_name+"]"
			result.append(apath)
			
		for filename in file_name_list:
			apath = filename
			result.append(apath)
		break
	return result

def main(argv):
	lsstr=all_path("e:\\")
	return lsstr


if __name__ == '__main__' :
	lsShow(main(sys.argv))	

			
