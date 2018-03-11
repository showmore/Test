# -*- coding: UTF-8 -*- 


def fib(m):
	n,a,b=0,0,1
	while n < m:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

if __name__ == '__main__':
	m=9
	L=[]
	for i in fib(m):
		L.append(i)
print(L[-1])


