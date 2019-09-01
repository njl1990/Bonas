#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import sys
import json


#LogLevel
LogLevel_Error = 1
LogLevel_Info = 4
LogLevel_Debug = 5



LogLevel = LogLevel_Debug

def debug(str):
	if LogLevel>=LogLevel_Debug:
		print('[Debug] '+str)

def info(str):
	if LogLevel>=LogLevel_Info:
		print('[Info] '+str)

def error(str):
	if LogLevel>=LogLevel_Info:
		print('[Error] '+str)