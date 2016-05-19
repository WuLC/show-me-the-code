# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-19 13:58:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 14:26:08
# @Email: liangchaowu5@gmail.com

import xlrd
import json
from lxml import etree

def read_xls(xls_file):
	book = xlrd.open_workbook(xls_file)
	sheet = book.sheet_by_index(0)
	content = []
	for i in xrange(sheet.nrows):
		#需要后面的json将unicode表示的中文转为正常中文显示
		tmp = '"'+sheet.row_values(i)[0]+'":"'+json.dumps(sheet.row_values(i)[1:]).decode('unicode-escape')+'"'
		content.append(tmp)
	con = """
{
%s
}
	"""%(',\n'.join(content))
	# print con
	return con


def write_xml(xls_content):
    root = etree.Element('root')
    comment = etree.Comment(u'\n学生信息表\n"id" : [名字, 数学, 语文, 英文]\n')
    root.append(comment)

    students = etree.Element('students') 
    root.append(students) 

    students.text = xls_content

    xml_content = etree.tostring(root, encoding= 'UTF-8', pretty_print=True, xml_declaration=True)

    with open('students.xml', 'wb') as f:
        f.write(xml_content)

if __name__ == '__main__':
	xls_file = '../0014/record.xls'
	#print read_xls(xls_file)
	write_xml(read_xls(xls_file))