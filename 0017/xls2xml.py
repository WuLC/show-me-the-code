# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-16 15:09:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 15:14:21
# @Email: liangchaowu5@gmail.com

# existing problem: " will be transfer to &quot; when writing content to xml

import xml.dom.minidom as md
import xlrd
import json


def read_xls(xls_file):
    book = xlrd.open_workbook(xls_file)
    sheet = book.sheet_by_index(0)
    content = []
    for i in xrange(sheet.nrows):
        #需要后面的json将unicode表示的中文转为正常中文显示
        tmp = '"'+sheet.row_values(i)[0]+'"'+' : '+json.dumps(sheet.row_values(i)[1:]).decode('unicode-escape') 
        content.append(tmp)
    con = """
{
%s
}
    """%(',\n'.join(map(lambda x:'\t'+x,content)))
    #print con
    return con


def write_xml(xls_content):
    xml_file = md.Document()
    root = xml_file.createElement('root') 
    students = xml_file.createElement('students') 
    xml_file.appendChild(root) 
    root.appendChild(students)

    comment = xml_file.createComment(u'\n学生信息表\n"id" : [名字, 数学, 语文, 英文]\n')
    students.appendChild(comment) 

    xml_content = xml_file.createTextNode(xls_content) 
    students.appendChild(xml_content)
    #print xml_file.toprettyxml(indent ="",encoding = 'UTF-8')
    
    with open('students.xml', 'wb') as f:
        f.write(xml_file.toprettyxml(indent ="",encoding = 'UTF-8'))
    
if __name__ == '__main__':
    xls_file = '../0014/record.xls'
    #print read_xls(xls_file)
    write_xml(read_xls(xls_file))
    

