# Reverse a string

a = 'abcdefge'
print a[::-1]

# Prob1.3
# Remove duplicate characters in a string with no additional buffer

# Prob 1.5
# Replace all spaces in a string with '%20'
def space_rep(s):
	space_ct = 0
	for i in range(len(s)):
		space_ct += (s[i] == ' ')
	newlen = len(s)+space_ct*2
	l = [None for i in xrange(newlen)]
	j = 0
	for i in range(len(s)):
		if s[i] != ' ':
			l[j] = s[i]
			j += 1
		else:
			l[j],l[j+1],l[j+2] = '%','2','0'
			j += 3
		#print l
	return ''.join(l)

s = 'Pengkai Ru is a PhD student.'
print space_rep(s)

