#!/usr/bin/python3

""" 
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. """

# Python code to generate random numbers and append them to a list 
import random 

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
 
#num = 10
#start = 20
#end = 40
#print(Rand(start, end, num)) 

list_1 = Rand(10,100,8)
list_2 = Rand(10,100,6)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list_1)
print(list_2)

output = []

for i in list_1 :
	if i in list_2 :
		if i not in output :
			output.append(i)
		
print(output)

