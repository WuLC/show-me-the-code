# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 22:26:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 11:14:02
# @Email: liangchaowu5@gmail.com

import json
import xlwt
json_file = 'city.txt'

with open(json_file) as f:
	data = json.load(f)

# the dict data is not sorted, the following line can sort the dict by key
data = sorted(data.items(),key = lambda x:x[0])

# data becomes a list of tuple now , which tuple represents a k,v of the dict 

xls_file = xlwt.Workbook()
sheet = xls_file.add_sheet('city_info')
for i in xrange(len(data)):
	for j in xrange(len(data[i])):
		sheet.write(i,j,data[i][j])
xls_file.save('city.xls')