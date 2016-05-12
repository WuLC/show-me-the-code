# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-11 22:22:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 23:24:33
# @Email: liangchaowu5@gmail.com

import sys
import easygui

# 设置系统编码为 UTF-8，处理中文乱码问题

reload(sys)
sys.setdefaultencoding('utf8')

forbidden = []
with open('filtered_words.txt') as f:
	forbidden = map(lambda x:x.strip().lower(), f.readlines())

while True:
	#inp = raw_input('input sth(ctrl+c to stop): ').strip() # raw_input 不能正确处理中文
	inp = easygui.enterbox('input sth(ctrl+c to stop)').strip()
	if any([i in inp for i in forbidden]):
		print 'Freedom'
	else:
		print 'Hunam Rights'
