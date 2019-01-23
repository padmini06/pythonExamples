"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""



_name= input("Enter your name\n")
_age = int(input("Enter you age \n"))

if _age > 100 :
	print("your age is greater than 100")
else:
	diff = 100-_age;
	print(_name + " will reach 100 after",diff,"years")