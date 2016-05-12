# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-12 22:57:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 23:28:29
# @Email: liangchaowu5@gmail.com

import sys
import easygui

reload(sys)
sys.setdefaultencoding('utf8')

forbidden = []
with open('filtered_words.txt') as f:
	forbidden = map(lambda x:x.strip().lower(), f.readlines())
	"""
	for line in f:
		forbidden.append(line.strip().lower())
    """
while True:
	inp = easygui.enterbox('input sth,click "Cancle" to stop').strip()
	forbid = False
	for i in forbidden:
		if i in inp:
		    print 'forbidden',inp.replace(i, '**')
		    forbid = True
		    break
	if not forbid:
		print inp