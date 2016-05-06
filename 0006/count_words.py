# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-27 22:37:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-06 17:25:34
# @Email: liangchaowu5@gmail.com
# @Function: remove stopwords and count the words in a English File


import re
import os

def load_stopwords(file_path):
    """load the stop words in English
    
    Args:
        file_path (str):stop words file path 
    
    Returns:
        set:a set containing all the stop words 
    """
    if not os.path.isfile(file_path):
        print '%s not found'%file_path
        return
    with open(file_path) as f:
        words = f.readlines()
    for i in xrange(len(words)):
        words[i]=words[i].rstrip()
    return set(words)


def count_words(file_path):
    """count the number of occurance for each word in a file except stopwords
    
    Args:
        file_path (str):path of a file to be checked 
    
    Returns:
        dictionary: number of occurance for each word
    """
    if not os.path.isfile(file_path):
    	print '%s not found'%file_path
    	return
    stopword_file = 'StopWords.txt'
    stopwords = load_stopwords(stopword_file)

    with open(file_path) as f:
    	text = f.readlines()

    str_text = ''.join(text)       
    pattern = re.compile('[a-zA-Z-]+')  
    word_list = re.findall(pattern,str_text)

    result_dict = {}
    for word  in word_list:
        if word.lower() in stopwords or len(word) == 1:
            continue
    	if word not in result_dict:
    		result_dict[word] = 0
    	result_dict[word] += 1
    return result_dict 
    


if __name__ == '__main__':   
	file = 'test.txt'
	result = count_words(file)
	for i in result:
		print i,result[i]



