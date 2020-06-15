# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

import os


def filePath(fileDir='data',fileName='login.yaml'):
	'''
	:param fileDir: 目录
	:param fileName:要操作的文件名称
	:return:当前上级目录+fileDir+fileName
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def writeContent(content,fileName):
	'''将文件写入data目录下，文件名自定义'''
	with open(filePath(fileName=fileName),'w') as f:
		f.write(str(content))

def readContent():
	'''读取data下的文件'''
	with open(filePath(fileName='bookId'),'r') as f:
		return f.read()