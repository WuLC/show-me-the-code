# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-25 10:59:54
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-25 16:14:37
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

# insert code to mysql
import MySQLdb
import sys

HOST = '127.0.0.1' 
PORT = 3306
USER = 'root'
PASSWD = '528578'
DB = 'hehe'
TABLE = 'activation_code'

def insert_to_mysql(record_count=8):
	"""import record_count pieces of records to redis
	
	Args:
	    record_count (int, optional): number of records to insert 
	
	Returns:
	    None
	"""
	try:
		conn = MySQLdb.connect(host = HOST,port=PORT,user=USER,passwd=PASSWD,db=DB)
	except Exception:
		print 'connect Exception'
		sys.exit(0)
	cursor = conn.cursor() # cursor can be reused
	# a transaction
	try:
		for i in xrange(record_count):
			record = activation_code_generaor()
			SQL = 'insert into %s values("%s")'%(TABLE,record)
			cursor.execute(SQL)
		conn.commit()  #InnoDB
	except Exception:
	    conn.rollback()	
	finally:
		cursor.close()
		conn.close()
	
	
if __name__ == '__main__':
	insert_to_mysql()

