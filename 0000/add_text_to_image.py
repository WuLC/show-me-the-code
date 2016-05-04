# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-22 08:59:27
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-22 10:59:50
# @Email: liangchaowu5@gmail.com
# library needed:pillow
# Referer:http://pillow.readthedocs.org/en/3.1.x/index.html

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('blog.jpg') # return an image object
width,height = img.size      # get image size
location = (width*3/4,0)	 # number location
num_size = width/5           # number size
draw = ImageDraw.Draw(img) 
message_count = 20
font = ImageFont.truetype("microsoft-yahei.ttf", num_size)
draw.text(xy=location,text=str(message_count),fill=(255,0,0),font=font)
"""
xy – Top left corner of the text.
text – Text to be drawn. If it contains any newline characters, the text is passed on to mulitiline_text()
fill – Color to use for the text,rgb(red, green, blue) where the color values are integers in the range 0 to 255
font – An ImageFont instance.
"""
img.save('result1.jpg')
