# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-08 16:46:27
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-08 16:55:52
# @Email: liangchaowu5@gmail.com

from bs4 import BeautifulSoup

with open('test.html') as f:
	text = f.read()

soup = BeautifulSoup(text, "html.parser")
urls = soup.find_all('a')
for i in urls:
	#print i 
	link = i.get('href')
	if link.startswith('http'): # remove js files etc.
		print link,i.text.encode('utf8')