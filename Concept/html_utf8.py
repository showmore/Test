# -*- coding: UTF-8 -*- 


def html_utf8(url,nf):
	lines=[]
	with open(url,'r',encoding='utf-8') as of:
		for line in of:
			lines.append(line)
	lines.insert(5,r'<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>'+'\n')
	s=''.join(lines)
	with open(nf,'w+',encoding='utf-8') as nf:
		nf.write (s)

if __name__ == '__main__':
	url='C:\\Python_Project\\xjr_html_5\\1\\0D200FC9924634D7E0535F598C71E504.html'
	nf='C:\\Python_Project\\xjr_html_5\\2\\0D200FC9924634D7E0535F598C71E504.html'
	html_utf8(url,nf)