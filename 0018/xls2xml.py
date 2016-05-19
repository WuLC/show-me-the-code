# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-19 10:35:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 10:58:27
# @Email: liangchaowu5@gmail.com

import xlrd
import json


def read_xls(file_path):
	xls = xlrd.open_workbook(file_path)
	sheet = xls.sheet_by_index(0)
	for i in xrange(sheet.nrows):
		#print map(lambda x:x.encode('utf8'),sheet.row_values(i))
		print json.dumps(sheet.row_values(i)).decode('unicode-escape')


if __name__ == '__main__':
	xls_file = '../0015/city.xls'
	read_xls(xls_file)