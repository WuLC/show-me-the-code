# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 22:26:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 22:30:53
# @Email: liangchaowu5@gmail.com

import json
import xlwt
json_file = 'city.txt'

with open(json_file) as f:
	data = json.load(f)

content = []
for k,v in data.items():
	content.append([k,v])

xls_file = xlwt.Workbook()
sheet = xls_file.add_sheet('city_info')
for i in xrange(len(content)):
	for j in xrange(len(content[i])):
		sheet.write(i,j,content[i][j])
xls_file.save('city.xls')