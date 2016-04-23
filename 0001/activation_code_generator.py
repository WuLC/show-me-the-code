# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-23 20:15:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-23 20:27:11
# @Email: liangchaowu5@gmail.com

import string
import random
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits

def activation_code_generaor(size=6,candidate_chars=upper_case+lower_case+digits):
	"""generate a random code from candidate_chars whose length is equal to size 
	
	Args:
	    size (int, optional): length of the code
	    candidate_chars (TYPE, optional): characters to be selected to generate the code
	
	Returns:
	    str: a  random code
	"""
	code = ''.join([random.choice(candidate_chars) for i in xrange(size)])#random.choice(list) picks an element from list randomly
	return code

if __name__ == '__main__':
	print activation_code_generaor.__doc__
	print activation_code_generaor()
	print activation_code_generaor()
	print activation_code_generaor()
