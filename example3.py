#!/usr/bin/python3

"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

_lst=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in _lst	:
	if num<5 :
		print(num)
				
my_list = [1, 3, "Michele", [5, 6, 7]]

my_list.append(100)
for element in my_list:
  print(element)