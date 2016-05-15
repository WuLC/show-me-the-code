# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-15 11:27:06
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-15 11:33:26
# @Email: liangchaowu5@gmail.com

import json
import xlwt

json_file = 'numbers.txt'

with open(json_file) as f:
	content = json.load(f)

xls_file = xlwt.Workbook()
sheet = xls_file.add_sheet('nums')
for i in xrange(len(content)):
	for j in xrange(len(content[i])):
		sheet.write(i, j, content[i][j])
xls_file.save('numbers.xls')