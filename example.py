#!/usr/bin/python3
print("hello")

x=""
x=input("enter your name \n")
print("Hello",x)

x=input("enter number 1 \n")
y=input("enter number 2 \n ")
if x>y:
	print("x is greater than y");
	print("anscscdsafasf")
else:
	print("y is greater than x");
	
	
def MaxNumber(a,b,c):
	"This function will return the max of the three value passed"
	if a>b and a>c : return a
	elif b>c and b>a : return b
	else:return c
	
max= MaxNumber(5,12,10)
print("Max number is :",max)
