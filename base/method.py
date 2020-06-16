# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

import requests

'''
API测试需要以下几个模块：
1.请求方法
2.请求地址
3.请求头
4.期望结果
'''
'''
存放数据的地方：
yaml -->tavern
excel
json
'''

class Requests():
	'''请求方法底层方法封装'''
	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**kwargs)
		if method=='post':
			return requests.request(url=url,method=method,**kwargs)
		if method=='put':
			return requests.request(url=url,method=method,**kwargs)
		if method=='delete':
			return requests.request(url=url,method=method,**kwargs)

	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)

	def put(self,url,**kwargs):
		return self.request(url=url,method='put',**kwargs)

	def delete(self,url,**kwargs):
		return self.request(url=url,method='delete',**kwargs)


