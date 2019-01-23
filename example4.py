#!/usr/bin/python3

"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""

def divisor(num):
	y=int(num/2)
	for i in range(1,y+1):
			if num%i == 0 :
				print (i)
	
	
x=int(input("Enter a number "))
divisor(x)