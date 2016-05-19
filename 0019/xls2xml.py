# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-19 14:53:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 15:13:56
# @Email: liangchaowu5@gmail.com

import xlrd
from lxml import etree


def read_xls(xls_file):
    xls = xlrd.open_workbook(xls_file)
    sheet = xls.sheet_by_index(0)
    content = []
    for i in xrange(sheet.nrows):
        line = map(lambda x:int(x),sheet.row_values(i))
        content.append(line)
    con ="""
{
%s
}
"""%(',\n'.join(map(lambda x:str(x),content)))
    return  con


def create_xml(xls_content):
    root = etree.Element('root')
    comment = etree.Comment(u'数字信息')
    root.append(comment)

    numbers = etree.Element('numbers')
    numbers.text = xls_content
    root.append(numbers)
    
    xml_content = etree.tostring(root, encoding='UTF-8', pretty_print=True, xml_declaration=True)
    with open('numbers.xml','w') as f:
        f.write(xml_content) 


if __name__ == '__main__':
    xls_file = '../0016/numbers.xls'
    xls_content = read_xls(xls_file)
    create_xml(xls_content)
