#!/usr/bin/python3

"""
Ask the user for a number and determine whether the number is prime or not
"""

def GetNumber(txt) :
	return int(input(txt))
	
def isPrime(x):
	for i in range(2,int(x/2 + 1)) :
		print (i)
		if x%2 == 0 :
			return False
	return True		
	
	
x= GetNumber("Enter a number")
if isPrime(x) == True :
	print ("%d is a prime number",x)
else :
	print ("%d is not a prime number",x)