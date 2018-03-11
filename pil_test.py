# coding:utf-8
# date:2018-01-30
# author:George

import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# 定义图片
img = Image.new('RGB',(150,50),(255,255,255))
#创建画笔
draw = ImageDraw.Draw(img)
#绘制点和线
for i in range(random.randint(1,10)):
	draw.line([(random.randint(1,150),random.randint(1,150)),(random.randint(1,150),random.randint(1,150))],fill = (0,0,0)) #定义线条颜色

#绘制点
for i in range(100):
	draw.point([random.randint(1,150),random.randint(1,150)],fill = (0,0,0))

#绘制文字
fontList = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

c_chars = ' '.join(random.sample(fontList,5))
font = ImageFont.truetype("simsun.ttc",28)
draw.text((8,8),c_chars,font = font,fill = 'green')

#扭曲
params = [\
1 - float(random.randint(1,2))/100,\
0,\
0,\
0,\
1 - float(random.randint(1,2))/100,\
float(random.randint(1,2))/500,\
0.001,\
float(random.randint(1,2))/500\
]

img = img.transform((150,50),Image.PERSPECTIVE,params)
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

img.show()
