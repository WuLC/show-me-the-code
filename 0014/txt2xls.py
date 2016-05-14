# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 21:39:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 22:13:15
# @Email: liangchaowu5@gmail.com

import json
import xlwt
json_file = 'student.txt'

def load_josn(json_file):
	"""parse json file, return a dictionary
	
	Args:
	    json_file (str): file path of the json file 
	
	Returns:
	    dict: data of the file in a dict form
	"""
	with open(json_file) as f:
		data = json.load(f)
	return data


def wirte_xls(data):
	"""create a xls file and write data into it
	
	Args:
	    data (dict): data in the form of a dict 
	
	Returns:
	    None
	"""
	# create xls file
	xls_file = xlwt.Workbook()
	sheet1 = xls_file.add_sheet('studeng info')
    
    # format the data to write it into xls file 
	content = []
	for k,v in data.items():
		content.append([k]+v)

	for i in xrange(len(content)):
		for j in xrange(len(content[i])):
			sheet1.write(i,j,content[i][j])
	xls_file.save('record.xls')


if __name__ == '__main__':
	wirte_xls(load_josn(json_file))



