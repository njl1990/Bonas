#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import sys
import json


#LogLevel:
LogLevel = 1

def debug(str):
	if LogLevel==1:
		print(str)