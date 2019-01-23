#!/usr/bin/python3

"""https://www.practicepython.org/
Odd Or Even """

def CheckOddEven(num):
	if num%2 == 0:
		print(num,"is even")
	else : 
		print(num,"is odd")

	
_num=int(input("Enter a number\n"))

CheckOddEven(_num)