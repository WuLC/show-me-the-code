# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-19 10:35:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 13:18:24
# @Email: liangchaowu5@gmail.com

import xlrd
import json
from lxml import etree


def read_xls(file_path):
	xls = xlrd.open_workbook(file_path)
	sheet = xls.sheet_by_index(0)
	content = []
	for i in xrange(sheet.nrows):
		line = '"'+sheet.row_values(i)[0]+'":"'+sheet.row_values(i)[1]+'"'
		content.append(line)
	content = """
{
%s
}
 """ %(',\n'.join(content))
	return content


def create_xml(content):
	root = etree.Element('root')
	comment = etree.Comment(u'城市信息')
	root.append(comment)
	second_element = etree.Element('cities')
	second_element.text = content
	root.append(second_element)
	
	xml_content = etree.tostring(root,encoding='UTF-8',pretty_print=True,xml_declaration=True)
	with open('cities.xml','w') as f:
		f.write(xml_content)


if __name__ == '__main__':
	xls_file = '../0015/city.xls'
	content = read_xls(xls_file)
	print create_xml(content)