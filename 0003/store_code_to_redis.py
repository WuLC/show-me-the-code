# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-25 16:08:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-25 20:13:23
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

# import record to redis
	
import redis
import sys

HOST = '110.64.76.112'
PORT =  6379
PASSWD = 'scutbaimi!2#4%'

def import_to_reids(record_count=8):
	"""import record_count pieces of records to redis with transaction
	
	Args:
	    record_count (int, optional): number of records to insert 
	
	Returns:
	    None
	"""
	try:
		conn = redis.Redis(host=HOST,port=PORT,password=PASSWD)
	except:
		print 'connection error'
		sys.exit(0)

	# add to a set,transaction with pipeline
	trans = conn.pipeline(transaction=True)   
	set_name = 'activation_code'
	try:
		for i in xrange(record_count):
			code = activation_code_generaor()
			trans.sadd(set_name,code)
		trans.execute() #commit all commands at a time
		# show the code
		print'success,number of keys in a set:',conn.scard(set_name)
	except:
		print 'error,rollback'
		sys.exit(0)

if __name__ == '__main__':
	import_to_reids()