# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

from base.method import Requests
from utils.operationExcel import *
from common.public import *
import pytest
import json


excel=OperationExcel()
obj=Requests()
'''把参数作为字典输出'''
@pytest.mark.parametrize('datas',excel.runs())

def test_login_book(datas):
	'''取出每次传入datas的期望状态码'''
	expect_status_code=datas[ExcelVarles.status_code]

	def case_assert(r,status_code):
		'''断言函数'''
		assert r.status_code==status_code
		assert datas[ExcelVarles.expect] in json.dumps(r.json(),ensure_ascii=False)

	def getUrl():
		'''针对url里面包含参数需要被替换，返回替换值'''
		return str(datas[ExcelVarles.caseUrl]).replace("{bookId}",readContent())


	'''对请求参数做序列化处理'''
	params=datas[ExcelVarles.params]
	if len(str(params).strip())>0:
		params=json.loads(params)

	'''对请求头的反序列化处理'''
	header=datas[ExcelVarles.headers]
	if len(str(header).strip())>0:
		header=json.loads(header,strict=False)

	'''1.获取前置条件的测试用例
	   2.执行前置测试用例
	   3.拿到它的token
	   4.拿它的结果信息替换对应测试点变量
	'''
	# 执行前置条件的测试，不管前置条件是否可以运行都有运行
	r=obj.post(url=excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl]
	           ,json=json.loads(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params]))
	# 获取到token
	prevResult=r.json()["access_token"]
	header=excel.newHeaders(prevResult=prevResult)

	if datas[ExcelVarles.method]=='post':
		r=obj.post(url=datas[ExcelVarles.caseUrl],headers=header,
		           json=params)
		writeContent(r.json()[0]["datas"]["id"],"bookId")
		case_assert(r,expect_status_code)

	if datas[ExcelVarles.method]=='get':
		if '/books' in datas[ExcelVarles.caseUrl]:
			r=obj.get(url=datas[ExcelVarles.caseUrl],headers=header)
			case_assert(r,expect_status_code)
		else :
			r = obj.get(url=getUrl(), headers=header)
			case_assert(r, expect_status_code)

	if datas[ExcelVarles.method]=='delete':
		r=obj.delete(url=getUrl(),headers=header)
		case_assert(r,expect_status_code)

	if datas[ExcelVarles.method]=='put':
		r = obj.put(url=getUrl(), headers=header,json=params)
		case_assert(r, expect_status_code)


if __name__=='__main__':
	# pytest.main(['-s','-v','test_login_token_book.py'])
	pytest.main(["-s", "-v", "test_login_token_book.py","--alluredir","./report/result"])
	import subprocess
	subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html',shell=True)

