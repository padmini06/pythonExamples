#!/usr/bin/python3

"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me."""


def getString(txt) :
	return (input(txt))
	

def reverseString(input_str):
	_list = input_str.split(" ")
	_rvsLst = _list[::-1]
	print(_rvsLst)
	result = " ".join(_rvsLst)
	print (result)
	
	
	
input_str = getString("Enter a string")
reverseString(input_str)
	