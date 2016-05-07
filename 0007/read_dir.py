# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-07 10:32:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 10:51:55
# @Email: liangchaowu5@gmail.com
# @Function: read dir and return paths of files with certain filename extension

import os

def read_dir(dir_path,result):
	"""return files path of the dir with certain  filename extension
	
	Args:
	    dir_path (str): dir of files 
	    result (list): path of files with certain filename  extension 
	
	Returns:
	    None
	"""
	filename_extension = ['.py','.java','.cpp']
	if not os.path.isdir(dir_path):
		print 'not a legal dir'
		return
	if dir_path[-1] == '/' and dir_path[-2]!=':':
		print 'remove the / at the end of the dir path'
		return
	for i in os.listdir(dir_path):
		f = dir_path+'/'+i
		if os.path.isfile(f):
			extension = os.path.splitext(i)[1]
			if extension in filename_extension:
				result.append(f)
		elif os.path.isdir(f):
			read_dir(f,result)

if __name__ == '__main__':
	dir_path = 'H:/'
	result = []
	read_dir(dir_path,result)
	for i in result:
		print i 
