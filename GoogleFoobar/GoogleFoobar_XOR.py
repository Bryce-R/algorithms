def answer(start, length):
	def f(a):
		l = [a,1,a+1,0]
		return l[a%4]

	result = 0;
	for i in xrange(length,0,-1):
		j = length -i
		result ^= (f(start+(j*length)-1)^f(start+(j*length)+i-1))
	return result
	








start = 0;
length = 3;
#start = 17;
#length = 4;
print answer(start,length)
# result = 0;
# print 0,result
# for i in xrange(1,10):
# 	result ^= i;
# 	print i,result
# 17 18 19 20 /
# 21 22 23 /  24
# 25 26 /  27 28
# 29 /  30 31 32

