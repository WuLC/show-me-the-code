# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-06 16:17:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-06 16:35:28
# @Email: liangchaowu5@gmail.com
# Function:read all the files' names of a given dir ,including the subdir

import os

def read_dir(dir_path,result):
	if not os.path.isdir(dir_path):
		print 'not a legal dir'
		return
	if dir_path[-1] == '/':
		print 'remove the / at the end of the dir path'
		return
	for i in os.listdir(dir_path):
		f = dir_path+'/'+i
		if os.path.isfile(f):
			result.append(f)
		elif os.path.isdir(f):
			read_dir(f,result)

if __name__ == '__main__':
	dir = "G:/corpusMini"
	result = []
	read_dir(dir,result)
	for i in result:
		print i

