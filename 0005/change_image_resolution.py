# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-04 15:02:23
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-04 15:42:41
# @Email: liangchaowu5@gmail.com

from PIL import Image

img = Image.open('blog.jpg')
width, height = img.size  # size of original image
print width,height

"""
# change size of image
pixel_size = (128, 128)
img.thumbnail(pixel_size)
img.save('result1.jpg')
"""

# change resolution of image
resolution = (100,100)
img.save("result2.jpg", dpi=resolution)
