# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

import yaml
from common.public import filePath

class OperationYaml(object):
	def readYaml(self):
		'''读取data目录下的yaml文件,对单个api进行测试时使用'''
		with open(filePath(),'r',encoding='utf-8')as f:
			'''返回的是list类型数据'''
			return list(yaml.safe_load_all(f))

	def dictYaml(self,fileDir='config',fileName='book.yaml'):
		'''针对多个api接口测试，测试用例放在excel中'''
		'''数据在excel文件，data部分在是放在config文件夹下的yaml文件'''
		with open(filePath(fileDir,fileName),'r',encoding='utf-8') as f:
			'''默认文件放在config文件夹下，默认文件名是login_xlsx.yaml'''
			'''返回的是字典类型数据'''
			return yaml.safe_load(f)

