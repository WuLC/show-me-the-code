# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-06 16:17:54
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-06 20:42:58
# @Email: liangchaowu5@gmail.com
# find the most important word of a file through TF-IDF

from count_words import count_words
from read_dir import read_dir

def get_tf(dir):
	"""get tf value for  words in each files of a dir
	
	Args:
	    dir (str): directory of the files 
	
	Returns:
	    dir_tf(dict): key is file path,value is also a dict,which contains tf values for the words of the file
	"""
	from math import log
	file_list = []
	read_dir(dir,file_list)
	dir_tf = {}
	for f in file_list:
		result = count_words(f)
		total = sum(result.values())
		for word in result:
			result[word] = log(float(total)/result[word],2)
		dir_tf[f]= result
	return dir_tf


def get_idf(dir):
	"""return idf value of all words in the files of a dir  
	
	Args:
	    dir (str):directory of the files
	
	Returns:
	    dir_idf(dict):words with their idf values
	"""
	file_list = []
	read_dir(dir,file_list)
	doc_num = len(file_list)
	dir_idf = {}
	for f in file_list:
		result = count_words(f)
		words = result.keys()
		for word in words:
			if word in dir_idf:
				dir_idf[word] += 1
			else:
				dir_idf[word] = 1
	for word in dir_idf:
		dir_idf[word] = float(dir_idf[word])/doc_num
	return dir_idf	


def get_keywords(dir,word_num):
	"""choose the  most important  words for each file in the dir
	
	Args:
	    dir (str): dir of files
	    word_num (int): words to be selected
	
	Returns:
	    tf_idf(dict): important words of each file in the dir
	"""
	tf = get_tf(dir)
	idf = get_idf(dir)
	tf_idf = {}
	for doc in tf:
		for word in tf[doc]:
			tf[doc][word] = tf[doc][word]*idf[word]
		tmp = sorted(tf[doc].items(),key = lambda x:x[1],reverse = True) #sort the dict in terms of value
		word_list = []
		for i in xrange(word_num):
			word_list.append(tmp[i][0])
		tf_idf[doc] = word_list
	return tf_idf

if __name__ == '__main__':
	dir = 'G:/corpusMini/test'
	result = get_keywords(dir,3)
	for i in result:
		print i,result[i]
