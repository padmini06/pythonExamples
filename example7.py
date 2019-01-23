#!/usr/bin/python3

"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""

import random

def randomList(start,end,size) :
	rd_list = []
	for i in range(size) :
		rd_list.append(random.randint(start,end))
	return rd_list

def check() :
	random_list = randomList(10,100,5)
	out_list = []
	for i in random_list :
		if i%2 == 0 :
			out_list.append(i)

	print (out_list)
		

	evenlist = [number for number in random_list if number % 2 == 0] 
	print (evenlist)
	# list comprehension 
	years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
	ages = [2014 - year for year in years_of_birth]

	print (ages)

if __name__=="__main__" :
	check()