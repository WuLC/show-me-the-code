# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-13 14:31:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-13 17:16:06
# @Email: liangchaowu5@gmail.com

# download images of a certain html page

import urllib2
import re

downloaded = set()  # avoid repeat download

def parse_page(url):
	"""parse the html page and find all the urls of image
	
	Args:
	    url (str): the url of html
	
	Returns:
	    list: all urls of images stored in a list
	"""
	try:
		f = urllib2.urlopen(url)
		content = f.read()
	except:
		print 'error while parsing page %s'%url
		return
    # jpg
	pattern = re.compile(r'https://pic(.*?).jpg')
	jpg_result = re.findall(pattern,content)
	img_srcs = map(lambda x:'https://pic'+x+'.jpg',jpg_result)
	# png
	pattern = re.compile(r'https://pic(.*?).png')
	png_result = re.findall(pattern,content)
	img_srcs += map(lambda x:'https://pic'+x+'.png',png_result)
	return img_srcs


def download_img(url, dir, num, log_file):
	"""download image of a certain url 
	
	Args:
	    url (str): url of the image
	    dir (str): local dir to store the image
	    num (int): the serial number of image downloaded,used to name the image
	    log_file (str): log file to record the images not downloaded successfully
	
	Returns:
	    None
	"""

	global downloaded # 防止重复下载
	if url in downloaded:
		return
	try:
		response = urllib2.urlopen(url)
		content = response.read()
	except urllib2.HTTPError, e:
		with open(log_file.decode('utf8'),'a') as f:
			f.write('error %s while downloading image %s \n'%(e.code,url))
		return
	except:
		with open(log_file.decode('utf8'),'a') as f:
			f.write('unexpected error while downloading image %s \n'%url)
		return

	if url.endswith('jpg'):
		suffix = '.jpg'
	else:
		suffix = '.png'
	file_path = dir+str(num)+suffix
	with open(file_path.decode('utf8'),'wb') as f:
		f.write(content)
		downloaded.add(url)
		print '%s downloaded successfully'%file_path


if __name__ == '__main__':
	#img_test_url = 'https://pic2.zhimg.com/0038a5d499a5463c59aad768200f18e1_b.png'
	root_url = 'https://www.zhihu.com/question/24340705'
	img_dir = 'D:/壁纸/手机壁纸/'
	log_file = img_dir+'download.log'
	urls = parse_page(root_url)

	for i in xrange(len(urls)):
		if  '"' in urls[i]:
			continue
		download_img(urls[i],img_dir,i,log_file)


