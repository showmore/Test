# -*- coding: UTF-8 -*-
import os
import logging

logger = logging.getLogger(__name__)

def get_picfiles():
    picfiles_tmp = ["/static/images/{}".format(x) for x in os.listdir('/home/george/myproject/code/Blog/static/images')]
    picfiles = [y for y in picfiles_tmp if y[-4:] == '.jpg']
    # logger.warning("pic file num is: {}".format(len(picfiles)))
    return picfiles
