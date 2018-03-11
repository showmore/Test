#coding:utf-8
import sys
import time
import urllib
import shutil
import requests
from PIL import Image
import pytesseract
from lxml import etree

im = Image.open("f:\\getCheckCode.do.jpg")
vcode = pytesseract.image_to_string(im)
print(vcode)

