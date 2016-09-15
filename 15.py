import sys
a=0
def fac(n):
	global a
	if n==0:
		return(1)
	else:
		a+=1
		return n*fac(n-1)
fac(int(input()))
print(a)
print(sys.getrecursionlimit())

