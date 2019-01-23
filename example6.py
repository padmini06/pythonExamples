#!/usr/bin/python3

"""Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)"""

def Palindrome(str):
	rvs=str[::-1] 		#string reverse
	if str == rvs :
		return True
	else :
		return False
	
	
def Reverse(str) :
	rvs_str = ""
	for w in range(len(str)):
		#print (w)
		#print (str[len(str)-1-w])
		rvs_str+=(str[len(str)-1-w])
	return rvs_str
		
		
str = input("Enter a string\n")
result = Palindrome(str)
if Palindrome(str) : 
	print("String is palindrome")
else :
	print ("String is not a palindrome")
	

reverse_str = Reverse(str)
if	reverse_str == str :
	print("String is palindrome")
else :
	print ("String is not a palindrome")
	
#print(reverse_str)