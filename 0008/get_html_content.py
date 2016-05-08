# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-08 15:31:51
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-08 16:52:03
# @Email: liangchaowu5@gmail.com

from bs4 import BeautifulSoup

with open('test.html') as f:
	text = f.read()

soup = BeautifulSoup(text, "html.parser")

# print soup.text.encode('utf8') # all html text

content = soup.find_all('p')
for i in content:
	#print isinstance(i.text,unicode)
	print i.text.encode('utf8')


