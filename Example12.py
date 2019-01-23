#!/usr/bin/python3

"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
 makes a new list of only the first and last elements of the given list"""
 
import example7
out_list = []

x_list = example7.randomList(10,100,5)
print(x_list)

out_list.append(x_list[0])
out_list.append(x_list[(len(x_list)-1)])

print (out_list)



