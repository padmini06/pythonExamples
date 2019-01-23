#!/usr/bin/python3
"""
Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
"""	

import random

def RandomList(start,end,size) :
	rd_list = []
	for i in range(size) :
		x=int(random.randint(start,end))
		rd_list.append(x)
	print (rd_list)
	return rd_list

	
a_list = RandomList(1,10,8)
b_list = RandomList(1,10,6)

out_list=[]

for i in a_list :
	if i not in b_list and i not in out_list:
		out_list.append(i)
		

	
print(out_list)
compherison_list = []
compherison_list = [ a for a in a_list if a not in b_list and a not in compherison_list]
print (compherison_list)
		