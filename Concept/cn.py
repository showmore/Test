# -*- coding: UTF-8 -*-
import sys
type = sys.getfilesystemencoding()
s='中文'
print s.decode('utf-8').encode(type)