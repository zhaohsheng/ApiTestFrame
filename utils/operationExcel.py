# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

import xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml
from common.public import *
import json

class ExcelVarles():
	caseID="测试用例ID"
	caseModel="模块"
	caseName="接口名称"
	caseUrl="请求地址"
	casePre="前置条件"
	method="请求方法"
	paramsType="请求参数类型"
	params="请求参数"
	expect="期望结果"
	isRun="是否运行"
	headers="请求头"
	status_code="状态码"

class OperationExcel():
	'''操作excel'''
	def getSheet(self):
		'''打开excel文件'''
		execl=xlrd.open_workbook(filePath('data','books.xlsx'))
		'''返回excel文件第一个sheet，将数据尽量放在第一个sheet里'''
		return execl.sheet_by_index(0)

	@property
	def getExcelDatas(self):
		'''获取excel的第一行也就是title'''
		title=self.getSheet().row_values(0)
		datas=[]
		'''将excel其他行作为列表输出，每行是一个字典'''
		for row in range(1,self.getSheet().nrows):
			row_values=self.getSheet().row_values(row)
			'''zip将两个数据搞成类似字典的元祖'''
			datas.append(dict(zip(title,row_values)))
		return  datas

	def runs(self):
		run_list=[]
		'''获取可执行测试用例:是否运行为y'''
		for item in self.getExcelDatas:
			isRun=item[ExcelVarles.isRun]
			if isRun=="y":
				run_list.append(item)
		return run_list

	def all_case(self):
		'''获取excel所有的测试用例'''
		run_list=[]
		'''获取可执行测试用例:是否运行为y'''
		for item in self.getExcelDatas:
			run_list.append(item)
		return run_list

	def params(self):
		params_list=[]
		for item in self.all_case():
			params = item[ExcelVarles.params]
			if len(str(params))>0:
				params_list.append(json.dumps(params))
		return params_list

	def case_prev(self,casePrev):
		'''
		根据前置条件找到管理的前置测试用例
		:param casePrev: 前置测试
		:return：返回前置测试用例的内容
		'''
		for item in self.all_case():
			if casePrev in item.values():
				return item
		return None

	def newHeaders(self,prevResult):
		'''
		替换请求头中的{token}
		:param prevResult: 被谁替换的谁
		:return:
		'''
		for item in self.runs():
			header=item[ExcelVarles.headers]
			if "{token}" in header:
				header=header.replace("{token}",prevResult)
				return json.loads(header)





