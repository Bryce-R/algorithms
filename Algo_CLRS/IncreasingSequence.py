# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:26:29 2016

@author: Pengkai
"""

def LIS(list,n):
	L = []
	L.append([list[0]])
	#global maxlen 
	#global k
	if n != 0:
		for ii in range(1,n+1):
			maxlen = 0
			k = 0
			for jj in range(0,ii):
				#print L[jj]
				if list[jj] < list[ii] and len(L[jj]) > maxlen:
					maxlen = len(L[jj])
					k = jj
			L.append(L[k] + [list[ii]])
			print L[ii]
	return L[n]
				

#n = int(raw_input("No. of intergers:"))
#str = raw_input("Please input all the integers:")
n = 9
str = "15 27 14 38 26 55 46 65 8"
# Separate all the integers
i = 0
list = []
for j in range(1,len(str)):
    #print j
    if str[j] == " " :
        list.append(int(str[i:j]))
        i = j+1
    elif j == len(str) -1:
        list.append(int(str[i:j+1]))
print "Entire list:"        
print list
#print LIS(list,0)

#maxlen = 0
LIS(list,n-1)
#print "LIS ending with 1st value of list:"
print LIS(list,1)
#print "Longest increasing subsequence."
print LIS(list,n-1)




