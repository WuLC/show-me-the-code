# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-27 22:37:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-27 23:26:19
# @Email: liangchaowu5@gmail.com
# @Function: count the words in a English File


import re
import os

def count_words(file_path):
    """count the number of occurance for each word in a file
    
    Args:
        file_path (str):path of a file to be checked 
    
    Returns:
        dictionary: number of occurance for each word
    """
    if not os.path.isfile(file_path):
    	print '%s not found'%file_path
    	return
    with open(file_path) as f:
    	text = f.readlines()

    str_text = ''.join(text)       
    pattern = re.compile('[a-zA-Z-]+')  
    result = re.findall(pattern,str_text)
    for i in result:
    	print i
    


if __name__ == '__main__':
	file = 'test.txt'
	count_words(file)



