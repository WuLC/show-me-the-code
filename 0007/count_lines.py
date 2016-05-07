# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-07 11:07:02
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 13:00:54
# @Email: liangchaowu5@gmail.com
# @Function: count the number of different types of line

from read_dir import  read_dir

def  count_lines(dir_path):
	file_list=[]
	result = {'code':0,'comment':0,'blank':0}
	read_dir(dir_path,file_list)
	print file_list
	for file in file_list:
		code = 0
		comment = 0
		blank = 0
		with open(file) as f:
			line = f.readline()
			while line != '':      # blank line is also judged True due to LF
				line=line.strip()  # remove blank space and LF
 				# blank line
				if line == '': 
				    blank += 1
				    line = f.readline()
				    continue

				# comment line
				# single line comment
				if line.startswith('//') or line.startswith('#') or ( line.startswith('/*') and line.endswith('*/') ):
					comment += 1
					line = f.readline()
					continue
				# multiple lines comment
				if line.startswith('/*'):
					comment += 1
					line = f.readline()
					while line!='':
						line=line.strip()
						comment += 1
						if line.endswith('*/'):
							break
						else:
							line = f.readline()
					if line == '': # read over  the file
						break
					line = f.readline()
					continue

				# code line
				code += 1
				line = f.readline()

		result['code'] += code
		result['comment'] += comment
		result['blank'] += blank
	return result		
				

if __name__ == '__main__':
	dir_path = 'H:/test'
	print count_lines(dir_path)
